"""
In PySide6 there seems actually no `pointSize` argument allowed when
contructing `QFont`! Although it's clearly defined in `QtGui.pyi`
and documented: https://doc.qt.io/qtforpython/PySide6/QtGui/QFont.html#PySide6.QtGui.PySide6.QtGui.QFont

On PySide2 it's going through but doesn't
do anything.
"""

try:
    from PySide2 import QtWidgets, QtGui
except ImportError:
    from PySide6 import QtWidgets, QtGui


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        w = QtWidgets.QWidget(self)
        self.setCentralWidget(w)
        vlyt = QtWidgets.QVBoxLayout(w)

        font1 = QtGui.QFont()
        font1.setPointSize(30)
        label1 = QtWidgets.QLabel('This is the first label.')
        label1.setFont(font1)
        vlyt.addWidget(label1)

        try:
            font2 = QtGui.QFont(pointSize=30)
            label2 = QtWidgets.QLabel('This is the second label.')
            label2.setFont(font2)
        except AttributeError as error:
            label2 = QtWidgets.QLabel(f'{error}')

        vlyt.addWidget(label2)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec_()
