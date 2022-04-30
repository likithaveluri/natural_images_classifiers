from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog
import sys
from PyQt5 import uic, QtGui, QtCore
from numpy import asarray
from PIL import Image
import tensorflow as tf
import numpy as np
import cv2;
from keras.models import model_from_json

class UI(QMainWindow):
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    def __init__(self):
        np.set_printoptions(suppress=True)

        super(UI, self).__init__()
        
        
        uic.loadUi('predictui.ui', self)
        
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")
        
        self.airplane = self.findChild(QLabel, "label_9")
        self.car = self.findChild(QLabel, 'label_10')
        self.cat = self.findChild(QLabel, 'label_11')
        self.dog = self.findChild(QLabel, 'label_12')
        self.flower = self.findChild(QLabel, 'label_13')
        self.fruit = self.findChild(QLabel, 'label_14')
        self.motorbike = self.findChild(QLabel, 'label_15')
        self.person = self.findChild(QLabel, 'label_16')



        
        
        self.button.clicked.connect(self.clicker)

        self.show()
        
   
        
    def clicker(self):

        fname = QFileDialog.getOpenFileName(self, "Open File", "", "Images (*png, *jpg)")

        if fname:
            new_model = tf.keras.models.load_model('saved_mdl/saved_model/modelthree')
            image = Image.open(fname[0]).convert('RGB')
            temp = np.array(image)
            cv2.imwrite("filename.png", temp)

            image = image.resize((180,180))
            image = np.array(image)
            

            pic = asarray(image)
            pic = pic.astype('float32')

            pic /= 255.0

            uu = np.array([pic])
            yy = new_model.predict(uu)
            yy = yy * 100
            print(type(yy))
            print(str(list(yy)[0]))

            pixmap = QtGui.QPixmap(fname[0])

            pixmap = pixmap.scaled(180, 180, QtCore.Qt.KeepAspectRatio)
            
            self.label.setPixmap(pixmap)
            self.label.show()

            self.airplane.setText('Aiplane: ' + str("{:.2f}".format(list(yy)[0][0])))
            self.airplane.adjustSize()

            self.car.setText('Car: ' + str("{:.2f}".format(list(yy)[0][1])))
            self.car.adjustSize()
            self.cat.setText('Cat: ' + str("{:.2f}".format(list(yy)[0][2])))
            self.cat.adjustSize()
            self.dog.setText('Dog: ' + str("{:.2f}".format(list(yy)[0][3])))
            self.dog.adjustSize()
            self.flower.setText('Flower: ' + str("{:.2f}".format(list(yy)[0][4])))
            self.flower.adjustSize()
            self.fruit.setText('Fruit: ' + str("{:.2f}".format(list(yy)[0][5])))
            self.fruit.adjustSize()
            self.motorbike.setText('Motorbike: ' + str("{:.2f}".format(list(yy)[0][6])))
            self.motorbike.adjustSize()
            self.person.setText('Person: ' + str("{:.2f}".format(list(yy)[0][7])))
            self.person.adjustSize() 

            

            
            
app = QApplication(sys.argv)

UIWindow = UI()

app.exec_()