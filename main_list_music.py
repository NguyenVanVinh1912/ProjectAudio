import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
from Danh_Sach_Nhac import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic= Ui_MainWindow()
        self.uic.setupUi(self)

        # self.uic.phat.clicked.connect(self.show_music)
    pygame
# Kết thúc game
pygame.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win=MainWindow()
    main_win.show()
    sys.exit(app.exec())