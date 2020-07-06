"""
Demo for "floating" widgets with Qt for Python.

The order of layout adding is not important! What counts is the order of widget
creation! Here the text label needs to be created first! Then the button Voila!
"""
from PySide2 import QtCore, QtWidgets
import floating_demo_ui


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()

        w = QtWidgets.QWidget(self)
        self.setCentralWidget(w)
        lyt = QtWidgets.QFormLayout(w)

        self.lw = QtWidgets.QWidget(self)
        self.ui = floating_demo_ui.Ui_Form()
        self.ui.setupUi(self.lw)

        self.ui.gridLayout.removeItem(self.ui.layout_1)
        self.ui.gridLayout.removeItem(self.ui.layout_0)

        self.ui.gridLayout.addLayout(self.ui.layout_0, 0, 0)
        self.ui.gridLayout.addLayout(self.ui.layout_1, 0, 0)
        self.ui.layout_1.setAlignment(
            self.ui.toolButton, QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight)

        lyt.addRow(self.lw)


def show():
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec_()


if __name__ == '__main__':
    show()
