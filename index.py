#import
import sys
import random
import Danh_Sach_Nhac ,nhac
import threading as th 
import pygame
import time  
from threading import Timer  
from music import *

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import main,nhac,Danh_Sach_Nhac

#xuly
ui=" "
app= QApplication(sys.argv)
MainWindow = QMainWindow()

def mainUi():
    global ui
    ui = main.UI_MainWindow()
    pygame.init()
    ui.setupUi()
    MainWindow.show()

mainUi()
sys.exit(app.exec())