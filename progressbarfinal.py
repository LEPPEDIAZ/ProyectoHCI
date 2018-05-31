#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a QProgressBar widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication, QDesktopWidget)
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.setStyleSheet("color: rgb(170, 0, 0);\n"
"background-color: rgb(170, 0, 0);")
    

        self.btn = QPushButton('pulse para cargar temperatura', self)
        self.btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(260, 260, 260, 160)
        #self.setStyleSheet("color: rgb(170, 0, 0);\n"
#"background-color: rgb(170, 0, 0);")
        self.setWindowTitle('Cargando')
        self.move(385,520)
        self.setFixedSize(260, 160) 
        self.show()
        
    def location_on_the_screen(self):    
        screen = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = screen.width() - widget.width()
        y = 2*screen.height() - widget.height()
        self.move(x, y)


        
        
    def timerEvent(self, e):
      
        if self.step >= 100:
            
            self.timer.stop()
            self.btn.setText('temperatura lista')
            sys.exit(pro.exec_())
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('temperatura pausada')
        else:
            self.timer.start(100, self)
            self.btn.setText('cargando...')
            
        
if __name__ == '__main__':
    
    pro = QApplication(sys.argv)
    ex = Example()
    sys.exit(pro.exec_())