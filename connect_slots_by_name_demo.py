from PySide6 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        self.button = QtWidgets.QPushButton(self)
        self.button.setObjectName('button')
        self.button.setText('Click Me!')
        layout.addWidget(self.button)

        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.Slot()
    def on_button_clicked(self):
        print(f'Hai from {self.sender()}')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec_()
