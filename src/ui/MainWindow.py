import os
import random

from PySide6 import QtCore, QtGui, QtWidgets

from genshin_impact_lottery.genshin_impact_lottery import MainWindow

from . import resource_rc
from .SpyderDialog import Ui_SpyderDialog
from .VideoDialog import Ui_VideoDialog


def gen_random_hex_color():
    hex_digits = '0123456789ABCDEF'

    return '#' + ''.join(
        random.choices(hex_digits, k=6)
    )


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__(None, QtCore.Qt.WindowType.Window)
        self.setupUi()

    def setupUi(self):
        color = gen_random_hex_color()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setFixedSize(self.width(), self.height())
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        font_button = QtGui.QFont()
        font_button.setPointSize(20)
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background.setPixmap(QtGui.QPixmap(u":/main_menu.png"))
        self.background.setScaledContents(True)
        self.Spyder = QtWidgets.QPushButton(self.centralwidget)
        self.Spyder.setGeometry(QtCore.QRect(200, 330, 200, 100))
        self.Spyder.setObjectName("Spyder")
        self.Spyder.setStyleSheet(
            f"border-image: url(:/spyder.png);\ncolor: 1f381b;")
        self.Spyder.setFont(font_button)
        self.Video = QtWidgets.QPushButton(self.centralwidget)
        self.Video.setGeometry(QtCore.QRect(420, 330, 200, 100))
        self.Video.setObjectName("Video")
        self.Video.setStyleSheet(
            f"border-image: url(:/video.png);\ncolor: 1f381b;")
        self.Video.setFont(font_button)
        self.genshin_impact_lottery = QtWidgets.QPushButton(self.centralwidget)
        self.genshin_impact_lottery.setGeometry(
            QtCore.QRect(305, 440, 200, 100))
        self.genshin_impact_lottery.setObjectName("genshin_impact_lottery")
        self.genshin_impact_lottery.setStyleSheet(
            f"border-image: url(:/lottery.png);\ncolor: 1f381b;")
        self.genshin_impact_lottery.setFont(font_button)
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(200, 170, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setObjectName("Title")
        self.Title.setStyleSheet("color: white;")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.init()

    def init(self):

        if not os.path.isfile("./list.txt"):
            self.genshin_impact_lottery.setEnabled(False)

        self.Spyder.clicked.connect(self.spyderWarper)
        self.Video.clicked.connect(self.videoWarper)
        self.genshin_impact_lottery.clicked.connect(
            self.genshin_impact_lottery_warper)

    def spyderWarper(self):
        spyderDialog = Ui_SpyderDialog(self)
        spyderDialog.show()

    def videoWarper(self):
        videoDialog = Ui_VideoDialog(self)
        videoDialog.show()

    def genshin_impact_lottery_warper(self):
        genshin_impact_lottery_dialog = MainWindow(self)
        genshin_impact_lottery_dialog.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "图像小助手"))
        self.Spyder.setText(_translate("MainWindow", "爬取图片"))
        self.Video.setText(_translate("MainWindow", "视频抽帧"))
        self.genshin_impact_lottery.setText(_translate("MainWindow", "随机抽取"))
        self.Title.setText(_translate("MainWindow", "图像小助手"))
