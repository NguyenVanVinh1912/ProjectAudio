import sys
import random
import threading as th 
import pygame
import time  
from threading import Timer  
# from timer import timer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
from nhac import Ui_MainWindow
from music import *
class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  
    
class MainWindow(QMainWindow):
    
    list = []
    __playMusic=False
    index = 0
    timer = ""
    callBackMusic = False
    temp = 0
    ran = False
   
    def __init__(self):
        super().__init__()
        self.uic= Ui_MainWindow()
        pygame.init()
        self.uic.setupUi(self)
        self.uic.phat.clicked.connect(self.show_music)
        self.uic.dung_lai.clicked.connect(self.stopMusic)
        self.uic.tam_dung.clicked.connect(self.pause_music)
        self.uic.lui_bai.clicked.connect(self.prevMusic)
        self.uic.lap_lai.clicked.connect(self.callBackMus)
        self.uic.chuyen_bai.clicked.connect(self.nextMusic)
        self.uic.ngau_nhien.clicked.connect(self.randomMusic)
        

        self.createList()
        #self.queuMusic()
        self.timer = RepeatTimer(1,self.display) 

        self.uic.noi_dung_mp3.setMinimum(0)
        self.uic.noi_dung_mp3.setValue(0)
      
        
        # #QMediaPlayer
        # self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('kk.mp3')))

        # #set Widget
        # self.videoWidget=QVideoWidget()
        # self.uic.verticalLayout.addWidget(self.videoWidget)
        # self.mediaPlayer.setVideoOutput(self.videoWidget)

    def randomMusic(self):
        if(self.ran == False):
            self.ran = True
        else:
             self.ran = False
    def callBackMus(self):
        if(self.callBackMusic == False):
            self.callBackMusic = True
        else:
             self.callBackMusic = False
     #dừng nhạc
    def stopMusic(self):
        self.timer.cancel()  
        pygame.mixer.music.stop() 
        self.__playMusic = False
    #hàng đợi nhạc
    def queuMusic(self):
        for value in self.list:
            pygame.mixer.music.queue(value.link)
    #hiển thị thời gian
    def tong_thoi_gian_bai_hat(danh_sach_thoi_gian):
        tong = 0
        for thoi_gian in danh_sach_thoi_gian:
            phut, giay = thoi_gian.split(":")
            tong += int(phut) * 60 + int(giay)
        return tong   

    def display(self):  
        mi = int(pygame.mixer.music.get_pos()/1000/60)
        if(mi < 10):
            mi = "0" + str(mi)
        second = int(pygame.mixer.music.get_pos()/1000%60)
        if(second < 10):
            second = "0" + str(second)
        
       
        if str(mi)+":"+str(second) == "00:59":
           self.temp += 1
        if self.temp == 2: 
            self.nextMusic()
            self.restartTimer()
            self.temp = 0
        print(str(mi)+":"+str(second)) 
        self.uic.time_label.setText( "{}:{}".format(mi, second))
        self.uic.noi_dung_mp3.setValue(int(second))
    #lui bài hát
    def prevMusic(self):
        if(self.callBackMusic == True):
            self.index = self.index
        elif(self.ran == True):
            self.index = self.random()
        elif self.index > 0:
            self.index -= 1   
        else:
            self.index = len(self.list)-1
        
        pygame.mixer.music.load(self.list[self.index].link)
        
        pygame.mixer.music.play()
        self.restartTimer()
    def restartTimer(self):
        self.timer.cancel()
        self.timer = RepeatTimer(1,self.display) 
        self.timer.start()
    # chuyển tiếp bài hát
    def nextMusic(self):
        if(self.callBackMusic == True):
            self.index = self.index
        elif(self.ran == True):
            self.index = self.random()
            
        elif self.index < len(self.list)-1:
            self.index += 1 
        else:
            self.index = 0
        pygame.mixer.music.load(self.list[self.index].link)
        pygame.mixer.music.play()
        self.restartTimer()
    def createList(self):
        self.list = [Music("Tìm em","./music/TimEm.mp3","","266"),
        Music("Tình đầu","./music/TinhDau.mp3","","292"),
        Music("Tình yêu khủng long","./music/TinhYeuKhungLong.mp3","","187"),
        Music("Tòng Phu","./music/TongPhu.mp3","","290"),
        Music("Trên tình bạn dưới tình yêu","./music/TrenTinhBanDuoiTinhYeu.mp3","","196")
        ]
    def random(self):
        return random.randint(0, len(self.list)-2)
    def currentime(self):
        print(pygame.mixer.music.get_pos()/1000)
    def pause_music(self):
        #dừng bài hát
        pygame.mixer.music.pause()
        self.timer.cancel()
        
    def show_music(self):
        # self.mediaPlayer.play()
        # Tải tệp nhạc vào bộ nhớ
        if(self.__playMusic == False):   
            pygame.mixer.music.load(self.list[self.index].link)
            time=self.list[self.index].duration
            self.uic.noi_dung_mp3.setMaximum(int(time))
            self.__playMusic = True
            pygame.mixer.music.play()
            self.restartTimer()
        else:
            pygame.mixer.music.unpause()
            self.restartTimer()
    


    pygame
# Kết thúc game
pygame.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win=MainWindow()
    main_win.show()
    sys.exit(app.exec())
