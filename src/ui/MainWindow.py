from PySide6 import QtCore, QtGui, QtWidgets

from .SpyderDialog import Ui_SpyderDialog
from .VideoDialog import Ui_VideoDialog


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__(None, QtCore.Qt.WindowType.Window)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setFixedSize(self.width(), self.height())
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.Spyder = QtWidgets.QPushButton(self.centralwidget)
        self.Spyder.setGeometry(QtCore.QRect(200, 330, 200, 100))
        self.Spyder.setObjectName("Spyder")
        self.Video = QtWidgets.QPushButton(self.centralwidget)
        self.Video.setGeometry(QtCore.QRect(420, 330, 200, 100))
        self.Video.setObjectName("Video")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(200, 170, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setObjectName("Title")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.init()

    def init(self):
        self.Spyder.clicked.connect(self.spyderWarper)
        self.Video.clicked.connect(self.videoWarper)

    def spyderWarper(self):
        spyderDialog = Ui_SpyderDialog(self)
        spyderDialog.show()

    def videoWarper(self):
        videoDialog = Ui_VideoDialog(self)
        videoDialog.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "图像小助手"))
        self.Spyder.setText(_translate("MainWindow", "爬取图片"))
        self.Video.setText(_translate("MainWindow", "视频抽帧"))
        self.Title.setText(_translate("MainWindow", "图像小助手"))
