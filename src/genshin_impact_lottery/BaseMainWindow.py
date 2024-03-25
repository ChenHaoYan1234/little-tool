# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QDialog, QFrame, QLabel, QPushButton,
                               QSizePolicy, QToolButton, QWidget)


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"genshin-impact-lottery")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.start = QWidget(self)
        self.start.setObjectName(u"start")
        self.start.setGeometry(QRect(0, 0, 1280, 720))
        self.background = QLabel(self.start)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1280, 720))
        self.background.setPixmap(QPixmap(u":/images/bg.jpg"))
        self.background.setScaledContents(True)
        self.one = QPushButton(self.start)
        self.one.setObjectName(u"one")
        self.one.setGeometry(QRect(320, 430, 181, 61))
        self.ten = QPushButton(self.start)
        self.ten.setObjectName(u"ten")
        self.ten.setGeometry(QRect(760, 430, 181, 61))
        self.video = QVideoWidget(self)
        self.video.setObjectName(u"video")
        self.video.setGeometry(QRect(0, 0, 1280, 720))
        self.one_result = QFrame(self)
        self.one_result.setObjectName(u"one_result")
        self.one_result.setGeometry(QRect(0, 0, 1280, 720))
        self.one_result.setFrameShape(QFrame.Shape.StyledPanel)
        self.one_result.setFrameShadow(QFrame.Shadow.Raised)
        self.name = QLabel(self.one_result)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(520, 270, 321, 141))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(50)
        self.name.setFont(font1)
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image = QLabel(self.one_result)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, 0, 1280, 720))
        self.image.setPixmap(QPixmap(u":/images/one.jpg"))
        self.image.setScaledContents(True)
        self.closeButton = QToolButton(self.one_result)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(1200, 10, 50, 50))
        font2 = QFont()
        font2.setFamilies([u"Sans Serif"])
        font2.setPointSize(20)
        self.closeButton.setFont(font2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("genshin-impact-lottery", u"随机抽取", None))
        self.one.setText(QCoreApplication.translate("genshin-impact-lottery", u"\u5355\u62bd", None))
        self.ten.setText(QCoreApplication.translate("genshin-impact-lottery", u"\u5341\u8fde\u62bd", None))
        self.closeButton.setText(QCoreApplication.translate("genshin-impact-lottery", u"X", None))
    # retranslateUi

