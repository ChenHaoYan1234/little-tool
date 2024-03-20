import os

from PySide6 import QtCore, QtWidgets

from util import noNone, video


class Ui_VideoDialog(QtWidgets.QDialog):
    def __init__(self, parent: QtWidgets.QMainWindow) -> None:
        super().__init__(parent, QtCore.Qt.WindowType.Dialog)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("VideoDialog")
        self.resize(400, 160)
        self.setFixedSize(self.width(), self.height())
        self.VideoLabel = QtWidgets.QLabel(self)
        self.VideoLabel.setGeometry(QtCore.QRect(20, 40, 35, 20))
        self.VideoLabel.setObjectName("VideoLabel")
        self.SaveDirLabel = QtWidgets.QLabel(self)
        self.SaveDirLabel.setGeometry(QtCore.QRect(20, 90, 60, 20))
        self.SaveDirLabel.setObjectName("SaveDirLabel")
        self.Cancel = QtWidgets.QPushButton(self)
        self.Cancel.setGeometry(QtCore.QRect(320, 130, 75, 25))
        self.Cancel.setObjectName("Cancel")
        self.Send = QtWidgets.QPushButton(self)
        self.Send.setGeometry(QtCore.QRect(240, 130, 75, 25))
        self.Send.setObjectName("Send")
        self.Video = QtWidgets.QLineEdit(self)
        self.Video.setGeometry(QtCore.QRect(50, 40, 260, 20))
        self.Video.setObjectName("Video")
        self.SaveDir = QtWidgets.QLineEdit(self)
        self.SaveDir.setGeometry(QtCore.QRect(75, 90, 235, 20))
        self.SaveDir.setObjectName("SaveDir")
        self.VideoButton = QtWidgets.QPushButton(self)
        self.VideoButton.setGeometry(QtCore.QRect(320, 40, 75, 25))
        self.VideoButton.setObjectName("VideoButton")
        self.SaveDirButton = QtWidgets.QPushButton(self)
        self.SaveDirButton.setGeometry(QtCore.QRect(320, 90, 75, 25))
        self.SaveDirButton.setObjectName("SaveDirButton")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.init()

    def init(self) -> None:
        self.Send.clicked.connect(self.videoWarper)
        self.Cancel.clicked.connect(self.closeWarper)
        self.VideoButton.clicked.connect(self.getVideoFile)
        self.SaveDirButton.clicked.connect(self.getSaveDir)

    def videoWarper(self):
        if self.Video.text() == "":
            noNone(self, "视频")
            return
        if self.SaveDir.text() == "":
            noNone(self, "保存目录")
            return
        video(self.Video.text(), self.SaveDir.text())
        return

    def closeWarper(self):
        self.close()

    def getVideoFile(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
            self, "打开文件", os.path.abspath("./"))[0]
        self.Video.setText(path)

    def getSaveDir(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "选择文件夹", os.path.abspath("./"))
        self.SaveDir.setText(path)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("VideoDialog", "视频抽帧"))
        self.VideoLabel.setText(_translate("VideoDialog", "视频："))
        self.SaveDirLabel.setText(_translate("VideoDialog", "输出目录："))
        self.Cancel.setText(_translate("VideoDialog", "取消"))
        self.Send.setText(_translate("VideoDialog", "确定"))
        self.VideoButton.setText(_translate("VideoDialog", "浏览"))
        self.SaveDirButton.setText(_translate("VideoDialog", "浏览"))
