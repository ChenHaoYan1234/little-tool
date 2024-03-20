import os

from PySide6 import QtCore, QtWidgets

from util import noNone, spyder


class Ui_SpyderDialog(QtWidgets.QDialog):
    def __init__(self, parent: QtWidgets.QMainWindow) -> None:
        super().__init__(parent, QtCore.Qt.WindowType.Dialog)
        self.setupUi()

    def setupUi(self) -> None:
        self.setObjectName("SpyderWindow")
        self.resize(600, 200)
        self.setFixedSize(self.width(), self.height())
        self.Spyder = QtWidgets.QPushButton(self)
        self.Spyder.setGeometry(QtCore.QRect(380, 160, 100, 30))
        self.Spyder.setObjectName("Spyder")
        self.Cancel = QtWidgets.QPushButton(self)
        self.Cancel.setGeometry(QtCore.QRect(490, 160, 100, 30))
        self.Cancel.setObjectName("Cancel")
        self.KeyWordLable = QtWidgets.QLabel(self)
        self.KeyWordLable.setGeometry(QtCore.QRect(20, 25, 60, 20))
        self.KeyWordLable.setObjectName("KeyWordLable")
        self.KeyWord = QtWidgets.QLineEdit(self)
        self.KeyWord.setGeometry(QtCore.QRect(80, 25, 400, 20))
        self.KeyWord.setObjectName("KeyWord")
        self.SaveDirLabel = QtWidgets.QLabel(self)
        self.SaveDirLabel.setGeometry(QtCore.QRect(20, 75, 70, 20))
        self.SaveDirLabel.setObjectName("SaveDirLabel")
        self.SaveDir = QtWidgets.QLineEdit(self)
        self.SaveDir.setGeometry(QtCore.QRect(90, 75, 390, 20))
        self.SaveDir.setObjectName("SaveDir")
        self.Dir = QtWidgets.QPushButton(self)
        self.Dir.setGeometry(QtCore.QRect(490, 70, 100, 30))
        self.Dir.setObjectName("Dir")
        self.NumberLabel = QtWidgets.QLabel(self)
        self.NumberLabel.setGeometry(QtCore.QRect(20, 125, 70, 20))
        self.NumberLabel.setObjectName("NumberLabel")
        self.Number = QtWidgets.QLineEdit(self)
        self.Number.setGeometry(QtCore.QRect(90, 125, 390, 20))
        self.Number.setObjectName("Number")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.init()
        self.default()

    def init(self) -> None:
        self.Spyder.clicked.connect(self.spyderWarper)
        self.Cancel.clicked.connect(self.closeWarper)
        self.Dir.clicked.connect(self.getDir)

    def default(self) -> None:
        self.Number.setText(str(10))

    def closeWarper(self):
        self.close()

    def getDir(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, "选择文件夹", os.path.abspath("./"))
        self.SaveDir.setText(path)

    def spyderWarper(self):
        if self.KeyWord.text() == "":
            noNone(self, "关键词")
            return
        if self.SaveDir.text() == "":
            noNone(self, "保存目录")
            return
        if self.Number.text() == "" or int(self.Number.text()) == 0:
            noNone(self, "图片张数")
            return
        spyder(self.KeyWord.text(), self.SaveDir.text(), int(self.Number.text()))
        return

    def callback(self, a0):
        pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("SpyderWindow", "爬取图片"))
        self.Spyder.setText(_translate("SpyderWindow", "确认"))
        self.Cancel.setText(_translate("SpyderWindow", "取消"))
        self.KeyWordLable.setText(_translate("SpyderWindow", "关键词:"))
        self.SaveDirLabel.setText(_translate("SpyderWindow", "保存目录:"))
        self.Dir.setText(_translate("SpyderWindow", "浏览"))
        self.NumberLabel.setText(_translate("SpyderWindow", "图片张数:"))
