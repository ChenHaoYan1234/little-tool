import sys
import typing
import multiprocessing

from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from util import TaskWorkerProcess,TaskQueue


def main() -> typing.NoReturn:
    multiprocessing.freeze_support()
    TaskWorkerProcess.start()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    exit_ = app.exec_()
    TaskQueue.put(None)
    while TaskWorkerProcess.is_alive():
        TaskWorkerProcess.join()
    TaskWorkerProcess.close()
    sys.exit(exit_)

if __name__ == "__main__":
    main()
