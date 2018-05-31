# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:44:36 2018

@author: Ana Lucia Diaz Leppe
"""

import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
import sys

class Music(QMainWindow):
    def __init__(self):
        super().__init__()
        self.music=C.QCoreApplication(sys.argv)

        url= C.QUrl.fromLocalFile("./orange.mp3")
        content= M.QMediaContent(url)
        self.player = M.QMediaPlayer()
        self.player.setMedia(content)
        self.player.play()
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
    ex = Music()
    sys.exit(app.exec_())
    #self.player.stateChanged.connect( music.quit )
#music.exec()