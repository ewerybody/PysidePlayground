import PySide2 as PySide
from PySide2 import QtWidgets
# # import PySide6 as PySide
# # from PySide6 import QtWidgets


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.setMinimumWidth(800)

        # as soon as the QMenuBar is built in disabled state
        self.setEnabled(False)
        menubar = self.menuBar()

        # the first menu will be unaffected
        menubar.addMenu("&Main")

        # but the second will throw these "qt.accessibility.core" warnings
        menu2 = menubar.addMenu('Warning Thrower Menu')

        menu2.addAction('sdfgsdfgsdf')
        self.setMenuBar(menubar)
        self.setEnabled(True)


if __name__ == '__main__':
    print('PySide.version: %s' % PySide.__version__)
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec_()
