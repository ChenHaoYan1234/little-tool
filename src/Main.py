import sys
import typing

from PyQt5 import QtCore, QtGui, QtWidgets

from MainWindow import Ui_MainWindow


def main() -> typing.NoReturn:
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
