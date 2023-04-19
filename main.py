import sys
import random
import threading as th 
import pygame
import time  
import ffmpeg
from threading import Timer  
# from timer import timer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
from nhac import Ui_MainWindow
from object.music import *
from volume import *
from SongDAO import *
from MusicController import *
class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  
    
class MainWindow(QMainWindow):
    
    
    list = []
    songDao = SongDao()
    controller = MusicController()
    __playMusic=False
    index = 0
    timer = ""
    callBackMusic = False
    temp = 0
    ran = False
    volumn = True
    valueVolumn = 50
    valueVolumnOld = 50
   
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
        self.uic.loa_active.clicked.connect(self.setVolumn)
        self.uic.volume.setValue(self.valueVolumn)
        self.uic.volume.valueChanged.connect(self.setValueVolumn)
        self.list = self.songDao.SelectList()
        self.timer = RepeatTimer(1,self.display) 

        self.uic.noi_dung_mp3.setMinimum(0)
        self.uic.noi_dung_mp3.setValue(0)
        self.add_guest()
        
        # #QMediaPlayer
        # self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('kk.mp3')))

        # #set Widget
        # self.videoWidget=QVideoWidget()
        # self.uic.verticalLayout.addWidget(self.videoWidget)
        # self.mediaPlayer.setVideoOutput(self.videoWidget)

    #bảng danh sách
    def add_guest(self):
        rowPosition = self.uic.table_list.rowCount()
        #chọn full
        self.uic.table_list.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.uic.table_list.insertRow(rowPosition)
        label = [
                 "Tên bài hát",
                "Thể loại",
                "Ca sĩ"
                 ]
        numcols = 3
        numrows = len(self.list)      
        self.uic.table_list.setRowCount(numrows)
        self.uic.table_list.setColumnCount(numcols)  
        self.uic.table_list.setHorizontalHeaderLabels(label)

        header = self.uic.table_list.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        index = 0
        for value in self.list:
            name = value.name
            type = self.controller.searchTypeId(value.idType)
            singer = self.controller.searchSingerId(value.idSinger)
            self.uic.table_list.setItem(index,0,QtWidgets.QTableWidgetItem(name))
            self.uic.table_list.setItem(index,1, QtWidgets.QTableWidgetItem(str(type)))
            self.uic.table_list.setItem(index,2,QtWidgets.QTableWidgetItem(str(singer)))
            index = index+1
    #thời gian thực
    def duration(self, song):
        return int(float((ffmpeg.probe(song)['format']['duration'])))
    # giá trị âm lượng
    def setValueVolumn(self):
        self.valueVolumn = self.uic.volume.value()
        set_master_volume(self.valueVolumn)
    #âm lượng 
    def setVolumn(self):
        if self.volumn == True:
            self.valueVolumnOld = self.valueVolumn
            self.uic.volume.setValue(0)
            self.volumn = False
        else:
            self.volumn = True
            self.uic.volume.setValue(self.valueVolumnOld)
    #bật tắt ngẫu nhiên
    def randomMusic(self):
        if(self.ran == False):
            self.ran = True
        else:
             self.ran = False
    #bật tắt lập lại
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
        self.uic.noi_dung_mp3.setValue(0)
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
        self.uic.time_label.setText( "{}:{}".format(mi, second))
        self.uic.noi_dung_mp3.setValue(int(mi)*60+int(second))
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
        #chơi nhạc
        self.playMusic()
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
        self.playMusic()
        self.restartTimer()
    def playMusic(self):
        image = self.list[self.index].image
        linkSong = self.list[self.index].link
        maxTime = self.duration(linkSong)
        pygame.mixer.music.load(linkSong)
        self.uic.label_2.setText(self.list[self.index].name)
        if(image != ""):
            self.uic.label.setPixmap(QtGui.QPixmap(image))
        else:
            self.uic.label.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))

        self.uic.noi_dung_mp3.setMaximum(maxTime)
        pygame.mixer.music.play()
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
            self.playMusic()
            self.restartTimer()
            self.__playMusic = True
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
