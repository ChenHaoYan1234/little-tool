# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ten.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QLabel, QToolButton, QWidget


class Ui_TenWidget(QWidget):
    def setupUi(self, TenWidget):
        if not TenWidget.objectName():
            TenWidget.setObjectName(u"Form")
        TenWidget.resize(1280, 720)
        self.background = QLabel(TenWidget)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 1280, 720))
        self.background.setPixmap(QPixmap(u":/images/ten.png"))
        self.background.setScaledContents(True)
        self.name_1 = QLabel(TenWidget)
        self.name_1.setObjectName(u"name_1")
        self.name_1.setGeometry(QRect(140, 150, 101, 401))
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        font.setPointSize(50)
        self.name_1.setFont(font)
        self.name_1.setStyleSheet(u"background-color: rgb(255, 120, 0);")
        self.name_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_2 = QLabel(TenWidget)
        self.name_2.setObjectName(u"name_2")
        self.name_2.setGeometry(QRect(240, 150, 101, 401))
        self.name_2.setFont(font)
        self.name_2.setStyleSheet(u"background-color: rgb(255, 120, 0);")
        self.name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_3 = QLabel(TenWidget)
        self.name_3.setObjectName(u"name_3")
        self.name_3.setGeometry(QRect(340, 150, 101, 401))
        self.name_3.setFont(font)
        self.name_3.setStyleSheet(u"background-color: rgb(145, 65, 172);")
        self.name_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_4 = QLabel(TenWidget)
        self.name_4.setObjectName(u"name_4")
        self.name_4.setGeometry(QRect(440, 150, 101, 401))
        self.name_4.setFont(font)
        self.name_4.setStyleSheet(u"background-color: rgb(145, 65, 172);")
        self.name_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_5 = QLabel(TenWidget)
        self.name_5.setObjectName(u"name_5")
        self.name_5.setGeometry(QRect(540, 150, 101, 401))
        self.name_5.setFont(font)
        self.name_5.setStyleSheet(u"background-color: rgb(53, 132, 228);")
        self.name_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_6 = QLabel(TenWidget)
        self.name_6.setObjectName(u"name_6")
        self.name_6.setGeometry(QRect(640, 150, 101, 401))
        self.name_6.setFont(font)
        self.name_6.setStyleSheet(u"background-color: rgb(53, 132, 228);")
        self.name_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_7 = QLabel(TenWidget)
        self.name_7.setObjectName(u"name_7")
        self.name_7.setGeometry(QRect(840, 150, 101, 401))
        self.name_7.setFont(font)
        self.name_7.setStyleSheet(u"background-color: rgb(53, 132, 228);")
        self.name_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_8 = QLabel(TenWidget)
        self.name_8.setObjectName(u"name_8")
        self.name_8.setGeometry(QRect(740, 150, 101, 401))
        self.name_8.setFont(font)
        self.name_8.setStyleSheet(u"background-color: rgb(53, 132, 228);")
        self.name_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_9 = QLabel(TenWidget)
        self.name_9.setObjectName(u"name_9")
        self.name_9.setGeometry(QRect(940, 150, 101, 401))
        self.name_9.setFont(font)
        self.name_9.setStyleSheet(u"background-color: rgb(53, 132, 228);")
        self.name_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_10 = QLabel(TenWidget)
        self.name_10.setObjectName(u"name_10")
        self.name_10.setGeometry(QRect(1040, 150, 101, 401))
        self.name_10.setFont(font)
        self.name_10.setStyleSheet(u"background-color: rgb(53, 132, 228);")
        self.name_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.closeButton = QToolButton(TenWidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(1150, 10, 61, 61))
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(20)
        self.closeButton.setFont(font1)

        self.retranslateUi(TenWidget)

        QMetaObject.connectSlotsByName(TenWidget)
    # setupUi

    def retranslateUi(self, TenWidget):
        TenWidget.setWindowTitle(QCoreApplication.translate("TenWidget", u"TenWidget", None))
        self.closeButton.setText(QCoreApplication.translate("TenWidget", u"X", None))
    # retranslateUi

