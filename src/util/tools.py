from PyQt5 import QtWidgets


def noNone(parent: QtWidgets.QWidget, varName: str):
    QtWidgets.QMessageBox.critical(parent, f"{varName}不能为空", f"{varName}不能为空,\n请输入{varName}",
                                   QtWidgets.QMessageBox.StandardButton.Ok, QtWidgets.QMessageBox.StandardButton.Ok)
    return
