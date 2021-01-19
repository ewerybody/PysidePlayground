from PySide2 import QtCore, QtWidgets
import ui_file


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.ui = ui_file.get_module(__file__)
        self.ui.setupUi(self)

    @QtCore.Slot()
    def on_pushButton_clicked(self):
        print('on_pushButton_clicked!!!!')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec_()
