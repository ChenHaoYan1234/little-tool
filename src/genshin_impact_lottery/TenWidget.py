from .BaseTenWidget import Ui_TenWidget


class TenWidget(Ui_TenWidget):
    def __init__(self, parent):
        self._parent = parent

        super(TenWidget, self).__init__(parent)
        self.setupUi(self)

        self.closeButton.clicked.connect(self.tenClose)

    def setName(self, names: list[str]):
        for i, name in enumerate(names):
            tmp = ""
            for c in name:
                tmp += c
                tmp += '\n'
            tmp = tmp[:-1]
            getattr(self, f"name_{i + 1}").setText(tmp)

    def tenClose(self):
        self._parent.start.setVisible(True)
        self.setVisible(False)
