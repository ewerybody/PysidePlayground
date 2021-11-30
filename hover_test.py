from PySide2 import QtCore, QtGui, QtWidgets


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

        self.check.setStyleSheet('QCheckBox:hover {background: red}')

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.check.toggle()
        return super().mousePressEvent(event)

    def enterEvent(self, event: QtCore.QEvent) -> None:
        QtWidgets.QApplication.sendEvent(self.check, event)
        hover_event = QtGui.QHoverEvent(
            QtGui.QHoverEvent.HoverEnter, QtCore.QPoint(0, 0), QtCore.QPoint(-1, -1)
        )
        QtWidgets.QApplication.sendEvent(self.check, hover_event)
        return super().enterEvent(event)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        QtWidgets.QApplication.sendEvent(self.check, event)
        hover_event = QtGui.QHoverEvent(
            QtGui.QHoverEvent.HoverLeave, QtCore.QPoint(-1, -1), QtCore.QPoint(0, 0)
        )
        QtWidgets.QApplication.sendEvent(self.check, hover_event)
        return super().leaveEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec_()
