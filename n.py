import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableView, QPushButton
from PyQt5.QtWidgets import QWidget,QVBoxLayout
from PyQt5.QtGui import QStandardItemModel,QStandardItem

class PlaylistWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Thiết kế giao diện
        self.setWindowTitle("Danh sách phát")
        self.resize(400, 300)
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.layout = QVBoxLayout(self.centralwidget)

        self.playlistTable = QTableView(self.centralwidget)
        self.layout.addWidget(self.playlistTable)

        self.addFileButton = QPushButton("Thêm file", self.centralwidget)
        self.layout.addWidget(self.addFileButton)

        # Kết nối sự kiện với mã lập trình
        self.addFileButton.clicked.connect(self.addFile)

        # Khởi tạo mô hình cho TableView
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Tên file"])
        self.playlistTable.setModel(self.model)

    def addFile(self):
        # Mở hộp thoại chọn tệp
        fileName, _ = QFileDialog.getOpenFileName(self, "Chọn file âm thanh", "", "Audio Files (*.mp3 *.wav)")

        # Nếu người dùng đã chọn một tệp
        if fileName:
            # Thêm tên file vào mô hình
            item = QStandardItem(fileName)
            self.model.appendRow(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlaylistWindow()
    window.show()
    sys.exit(app.exec_())