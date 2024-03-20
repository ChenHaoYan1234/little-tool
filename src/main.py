import sys
import typing

from PySide6 import QtWidgets

from ui import Ui_MainWindow


def main() -> typing.NoReturn:
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    exit_code= app.exec()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
