import os
import sys
import platform
from PySide6 import QtCore, QtWidgets


class Demo(QtWidgets.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle(self.__class__.__name__)
        self.setMinimumSize(300, 200)
        layout = QtWidgets.QVBoxLayout(self)
        # layout.addWidget()


if __name__ == '__main__':
    sys.argv.extend(('-platform', 'windows:darkmode=1'))
    app = QtWidgets.QApplication([])
    main = Demo()
    main.show()
    app.exec()
