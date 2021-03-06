# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:21:06 2018

@author: Ana Lucia Diaz Leppe
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
import PyQt5.QtMultimedia as M
import PyQt5.QtCore as C
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.music=C.QCoreApplication(sys.argv)

        url= C.QUrl.fromLocalFile("./orange.mp3")
        content= M.QMediaContent(url)
        self.player = M.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()
        self.title = 'PyQt absolute positioning - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        label = QLabel('Python', self)
        label.move(50,50)
 
        label2 = QLabel('PyQt5', self)
        label2.move(100,100)
 
        label3 = QLabel('Examples', self)
        label3.move(150,150)
 
        label4 = QLabel('pytonspot.com', self)
        label4.move(200,200)
 
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())