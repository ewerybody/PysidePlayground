"""
Example showing how to use `QMetaObject.connectSlotsByName` to auto-connect
Python methods to matching widgets manually without ui-compiling.

* use `setObjectName()` on triggering widget
* call `QtCore.QMetaObject.connectSlotsByName(self)` passing self as main widget.
* make your methods slots via `@QtCore.Slot()`
* name your methods `on _ Qt-object-name _ Signal-name`
"""
from PySide6 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)

        # One actually does NOT need to make it a member of `self.`!
        # Also passing `self` for parenting is optional!
        hsdbfhjvbs = QtWidgets.QPushButton()

        # Setting the Qt object name is mandatory for this to work!
        # The python object name is irrelevant tho!
        hsdbfhjvbs.setObjectName('button')

        hsdbfhjvbs.setText('Click Me!')
        layout.addWidget(hsdbfhjvbs)

        # Passing `self` here is needed!
        QtCore.QMetaObject.connectSlotsByName(self)

    # You NEED to make this a `QtCore.Slot` to work!
    @QtCore.Slot()
    # the name pattern needs to be:
    # on _ Qt-object-name _ Signal-name
    def on_button_clicked(self):
        print(f'Hai from {self.sender()}')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec_()
