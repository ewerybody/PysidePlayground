"""
Example showing how to use auto-connecting Python methods/functions to
matching widgets with the `QMetaObject.connectSlotsByName` call thats compiled
into the python-Ui code.

The code generator always gives Qt object names! No need to care about that.
This way you merely need to make your methods fit like:
* make them slots via `@QtCore.Slot()`
* name them like `on _ Qt-object-name _ Signal-name`
"""
from PySide2 import QtCore, QtWidgets
import ui_file


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.ui = ui_file.get_module(__file__)
        self.ui.setupUi(self)

    # You NEED to make this a `QtCore.Slot` to work!
    @QtCore.Slot()
    # the name pattern needs to be:
    # on _ Qt-object-name _ Signal-name
    def on_pushButton_clicked(self):
        print('on_pushButton_clicked!!!!')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec_()
