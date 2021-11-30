"""
Trying to make another widget appear as if the mouse pointer is hovering.
"""

from PySide2 import QtCore, QtGui, QtWidgets


STYLE = 'QCheckBox {background: transparent} QCheckBox:hover {background: red;}'


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        blank = QtWidgets.QLabel('Thanks <b>dbunk</b>!! 🙏')
        blank.setFont(QtGui.QFont('', 40))
        blank.setMinimumSize(500, 200)
        layout.addWidget(blank)

        self.check = CBox('i wanna be hovered!')
        self.check.left.connect(self.send_hover)
        hlayout = QtWidgets.QHBoxLayout()
        hlayout.addWidget(self.check)
        # layout.addWidget(self.check)
        hlayout.addWidget(QtWidgets.QWidget())
        hlayout.setStretch(1, 1)
        layout.addLayout(hlayout)

        self.check.setStyleSheet(STYLE)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.check.toggle()
        return super().mousePressEvent(event)

    def send_hover(self, event=None):
        if event is None:
            pos = QtCore.QPoint(0, 0)
            event = QtGui.QEnterEvent(pos, pos, pos)
        QtWidgets.QApplication.sendEvent(self.check, event)
        hover_event = QtGui.QHoverEvent(
            QtGui.QHoverEvent.HoverEnter, QtCore.QPoint(0, 0), QtCore.QPoint(-1, -1)
        )
        QtWidgets.QApplication.sendEvent(self.check, hover_event)

    def enterEvent(self, event: QtCore.QEvent) -> None:
        self.check.cheat = True
        self.send_hover(event)
        return super().enterEvent(event)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        self.check.cheat = False
        hover_event = QtGui.QHoverEvent(
            QtGui.QHoverEvent.HoverLeave, QtCore.QPoint(-1, -1), QtCore.QPoint(0, 0)
        )
        QtWidgets.QApplication.sendEvent(self.check, event)
        QtWidgets.QApplication.sendEvent(self.check, hover_event)
        return super().leaveEvent(event)


class CBox(QtWidgets.QCheckBox):
    left = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cheat = False

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        if self.cheat:
            self.left.emit()
        return super().leaveEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec_()
