import random

from . import resource_rc
from .BaseMainWindow import Ui_MainWindow
from PySide6 import QtMultimedia
from PySide6.QtCore import QSize, QUrl
from .TenWidget import TenWidget

class MainWindow(Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setFixedSize(QSize(1280, 720))

        self.media_player = QtMultimedia.QMediaPlayer(self.video)
        self.media_player.setVideoOutput(self.video)
        self.audio_output = QtMultimedia.QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        self.ten_result = TenWidget(self)

        self.video.setVisible(False)
        self.one_result.setVisible(False)
        self.ten_result.setVisible(False)

        self.name.raise_()
        self.closeButton.raise_()

        self.one.clicked.connect(self.oneClicked)
        self.ten.clicked.connect(self.tenClicked)

        self.setupList()

    def setupList(self):
        with open("list.txt", encoding="utf-8") as f:
            self.list = f.read().splitlines()

    def oneClosed(self):
        self.start.setVisible(True)
        self.one_result.setVisible(False)

    def onePlayed(self, status):
        if status == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.one_result.setVisible(True)
            self.video.setVisible(False)
            self.name.setText(random.choice(self.list))
            try:
                self.closeButton.clicked.disconnect()
            except:
                pass
            self.closeButton.clicked.connect(self.oneClosed)

    def oneClicked(self):
        self.video.setVisible(True)
        self.start.setVisible(False)
        self.media_player.setSource(QUrl("qrc:/videos/one.mp4"))
        try:
            self.media_player.mediaStatusChanged.disconnect()
        except:
            pass
        self.media_player.mediaStatusChanged.connect(self.onePlayed)
        self.media_player.setPosition(0)
        self.media_player.play()

    def tenPlayed(self, status):
        if status == QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia:
            self.ten_result.setVisible(True)
            self.video.setVisible(False)
            self.choiceList = random.choices(self.list, k=10)
            self.ten_result.setName(self.choiceList)

    def tenClicked(self):
        self.video.setVisible(True)
        self.start.setVisible(False)
        self.media_player.setSource(QUrl("qrc:/videos/ten.mp4"))
        try:
            self.media_player.mediaStatusChanged.disconnect()
        except:
            pass
        self.media_player.mediaStatusChanged.connect(self.tenPlayed)
        self.media_player.setPosition(0)
        self.media_player.play()
