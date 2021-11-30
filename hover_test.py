from PySide2 import QtCore, QtGui, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        blank = QtWidgets.QWidget()
        blank.setMinimumSize(500, 200)
        layout.addWidget(blank)
        self.check = QtWidgets.QCheckBox('i wanna be hovered!')
        layout.addWidget(self.check)

        self.check.setStyleSheet('QCheckBox:hover {background: red}')

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.check.toggle()
        return super().mousePressEvent(event)

    def enterEvent(self, event: QtCore.QEvent) -> None:
        pos = self.check.geometry().center()
        print('pos: %s' % pos)
        hover_event = QtGui.QHoverEvent(QtGui.QHoverEvent.HoverEnter, pos, pos)
        QtWidgets.QApplication.sendEvent(self.check, hover_event)
        return super().enterEvent(event)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        pos = self.check.geometry().center()
        print('pos: %s' % pos)
        hover_event = QtGui.QHoverEvent(QtGui.QHoverEvent.HoverLeave, pos, pos)
        QtWidgets.QApplication.sendEvent(self.check, hover_event)
        return super().leaveEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec_()
