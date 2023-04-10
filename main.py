import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow,QFileDialog
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from nhac import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic= Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.phat.clicked.connect(self.show_music)
        # self.uic.add_file.clicked.connect(self.addFile)

        # #QMediaPlayer
        # self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('kk.mp3')))

        # #set Widget
        # self.videoWidget=QVideoWidget()
        # self.uic.verticalLayout.addWidget(self.videoWidget)
        # self.mediaPlayer.setVideoOutput(self.videoWidget)

        # self.model = QStandardItemModel()
        # self.model.setHorizontalHeaderLabels(["Tên file"])
        # self.list_song.setModel(self.model)
    
    def show_music(self):
        # self.mediaPlayer.play()
        # Tải tệp nhạc vào bộ nhớ
        
        pygame.init()
        pygame.mixer.music.load("kk.mp3")
        # Phát nhạc
        pygame.mixer.music.play()
    
    # def addFile(self):
    #     # Mở hộp thoại chọn tệp
    #     fileName, _ = QFileDialog.getOpenFileName(self, "Chọn file âm thanh", "", "Audio Files (*.mp3 *.wav)")

    #     # Nếu người dùng đã chọn một tệp
    #     if fileName:
    #         # Thêm tên file vào mô hình
    #         item = QStandardItem(fileName)
    #         self.model.appendRow(item)

   
# Kết thúc game
pygame.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win=MainWindow()
    main_win.show()
    sys.exit(app.exec())