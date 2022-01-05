"""
Trying to make another widget appear as if the mouse pointer is hovering.
"""

from PySide6 import QtCore, QtGui, QtWidgets


STYLE = 'QCheckBox {background: transparent} QCheckBox:hover {background: red;}'


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        layout = QtWidgets.QVBoxLayout(self)
        blank = QtWidgets.QLabel('Thanks <b>dbunk</b>!! 🙏<br>Thanks <b>Keith Kyzivat</b>!')
        blank.setFont(QtGui.QFont('', 25))
        blank.setMinimumSize(500, 200)
        layout.addWidget(blank)

        self.check = QtWidgets.QCheckBox('i wanna be hovered!')
        self.check.installEventFilter(self)
        self.check_allow_leave = False

        """add whole checkbox so it extends horizontally
        [(x) check label text                            ]
        """
        layout.addWidget(self.check)

        """or add in sub layout so it just occupies the text label space
        [(x) check label text][blank widget              ]
        """
        # hlayout = QtWidgets.QHBoxLayout()
        # hlayout.addWidget(self.check)
        # hlayout.addWidget(QtWidgets.QWidget())
        # hlayout.setStretch(1, 1)
        # layout.addLayout(hlayout)

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

    def eventFilter(self, _source, event):
        if event.type() in (QtCore.QEvent.Leave, QtGui.QHoverEvent):
            if not self.check_allow_leave:
                self.send_hover()
            return False
        return False

    def enterEvent(self, event: QtCore.QEvent) -> None:
        self.send_hover(event)
        self.check_allow_leave = False
        return super().enterEvent(event)

    def leaveEvent(self, event: QtCore.QEvent) -> None:
        self.check_allow_leave = True
        hover_event = QtGui.QHoverEvent(
            QtGui.QHoverEvent.HoverLeave, QtCore.QPoint(-1, -1), QtCore.QPoint(0, 0)
        )
        QtWidgets.QApplication.sendEvent(self.check, event)
        QtWidgets.QApplication.sendEvent(self.check, hover_event)
        return super().leaveEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec()
