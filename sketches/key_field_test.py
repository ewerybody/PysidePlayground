from PySide6 import QtWidgets


class Demo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.__class__.__name__)
        self.setMinimumSize(300, 200)
        layout = QtWidgets.QVBoxLayout(self)
        keyseqed = QtWidgets.QKeySequenceEdit(self)
        layout.addWidget(keyseqed)

        keyseqed.editingFinished.connect(self._on_keyseq_change)
        # keyseqed.keySequenceChanged.connect(self._on_keyseq_change)

    def _on_keyseq_change(self, *args):
        ked = self.sender()
        if not isinstance(ked, QtWidgets.QKeySequenceEdit):
            return
        print(ked.keySequence())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Demo()
    main.show()
    app.exec()
