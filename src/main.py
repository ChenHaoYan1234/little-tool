import multiprocessing
import sys
import typing

from PySide6 import QtWidgets

from ui import Ui_MainWindow
from util import TaskQueue, TaskWorkerProcess


def main() -> typing.NoReturn:
    multiprocessing.freeze_support()
    TaskWorkerProcess.start()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    exit_code= app.exec()
    TaskQueue.put(None)
    while TaskWorkerProcess.is_alive():
        TaskWorkerProcess.join()
    TaskWorkerProcess.close()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
