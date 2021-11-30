from PySide2 import QtCore, QtGui, QtWidgets


STYLE_HOVER = 'QCheckBox {background: rgba(255, 0, 0, 150);} QCheckBox:hover {background: red;}'
STYLE_NONE = 'QCheckBox {background: transparent} QCheckBox:hover {background: red;}'


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        blank = QtWidgets.QLabel('Thanks <b>dbunk</b>!! 🙏')
        blank.setFont(QtGui.QFont('', 40))
        blank.setMinimumSize(500, 200)
        layout.addWidget(blank)
        self.check = QtWidgets.QCheckBox('i wanna be hovered!')
        layout.addWidget(self.check)

        self.check.setStyleSheet(STYLE_NONE)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.check.toggle()
        return super().mousePressEvent(event)

    def enterEvent(self, event: QtCore.QEvent) -> None:
        self.check.setStyleSheet(STYLE_HOVER)
        return super().enterEvent(event)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        self.check.setStyleSheet(STYLE_NONE)
        return super().leaveEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec_()
