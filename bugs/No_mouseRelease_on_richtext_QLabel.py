from PySide6 import QtCore, QtWidgets, QtGui


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        w = QtWidgets.QWidget(self)
        w.setMinimumSize(350, 200)
        self.setCentralWidget(w)
        lyt = QtWidgets.QFormLayout(w)
        self.setWindowTitle('HoverWidget Demo')

        defaullt_text = (
            'Wrapped super long checkbox text text text text ... 😛'
            'Wrapped super long checkbox text text text text ...'
        )
        fancy_check1 = FancyCheck(defaullt_text)
        lyt.addRow(fancy_check1)

        richtext = 'Rich text <b>on a Checkbox</b>!!<br>With linebreaks!🤯'
        fancy_check2 = FancyCheck(richtext)
        lyt.addRow(fancy_check2)

        label = QtWidgets.QLabel('Default text just turned `QtCore.Qt.RichText`')
        label.setTextFormat(QtCore.Qt.RichText)
        fancy_check3 = FancyCheck()
        fancy_check3.hover.add_widget(label)
        lyt.addRow(fancy_check3)

        mdtext = 'Markdown text **on a Checkbox**!!  \rWith linebreaks!🤯'
        label = QtWidgets.QLabel(mdtext)
        label.setTextFormat(QtCore.Qt.MarkdownText)
        fancy_check5 = FancyCheck()
        fancy_check5.hover.add_widget(label)
        lyt.addRow(fancy_check5)

        self.check_pressed = _PressedIndicator('Mouse Pressed')
        self.check_released = _PressedIndicator('Mouse Released')
        for check in fancy_check1, fancy_check2, fancy_check3, fancy_check5:
            check.hover.mouse_pressed.connect(self.check_pressed.trigger)
            check.hover.mouse_released.connect(self.check_released.trigger)
        hlyt = QtWidgets.QHBoxLayout()
        hlyt.addWidget(self.check_pressed)
        hlyt.addWidget(self.check_released)
        lyt.addRow(hlyt)


class FancyCheck(QtWidgets.QWidget):
    def __init__(self, text='', parent=None):
        super().__init__(parent)
        self.hlayout = QtWidgets.QHBoxLayout(self)
        self.hlayout.setContentsMargins(0, 0, 0, 0)
        self.check = QtWidgets.QCheckBox(self)
        self.hlayout.addWidget(self.check)

        self.hover = HoverWidget(self)
        self.hover.set_hover_widget(self.check)
        if text:
            self.label = QtWidgets.QLabel(text)
            self.label.setWordWrap(True)
            self.hover.add_widget(self.label)
        self.hover.clicked.connect(self.check.toggle)
        self.hlayout.addWidget(self.hover)
        self.hlayout.setStretch(1, 1)


class HoverWidget(QtWidgets.QWidget):
    clicked = QtCore.Signal()
    context_menu_requested = QtCore.Signal()

    mouse_pressed = QtCore.Signal()
    mouse_released = QtCore.Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.hlayout = QtWidgets.QHBoxLayout(self)
        # self.hlayout.setContentsMargins(0, 0, 0, 0)
        self._hover_widget = None

    def set_hover_widget(self, widget):
        self._hover_widget = widget

    def add_widget(self, widget):
        self.hlayout.addWidget(widget)

    def enterEvent(self, event):
        self._send_hover_event(event)
        return super().enterEvent(event)

    def leaveEvent(self, event):
        if self._send_hover_event(event):
            self._hover_widget.setDown(False)
        return super().leaveEvent(event)

    def _send_hover_event(self, event):
        if self._hover_widget is None:
            return False

        pos = self._hover_widget.pos()
        pos1 = QtCore.QPoint(-1, -1)
        if event.type() == QtCore.QEvent.Enter:
            hovevent = QtGui.QHoverEvent(QtGui.QHoverEvent.HoverLeave, pos, pos1)
        else:
            hovevent = QtGui.QHoverEvent(QtGui.QHoverEvent.HoverLeave, pos1, pos)
        QtWidgets.QApplication.sendEvent(self._hover_widget, hovevent)
        QtWidgets.QApplication.sendEvent(self._hover_widget, event)
        return True

    def mousePressEvent(self, event):
        self.mouse_pressed.emit()
        if self._hover_widget is not None:
            if self._hover_widget.isEnabled() and event.button() == QtCore.Qt.LeftButton:
                self._hover_widget.setDown(True)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.mouse_released.emit()
        if event.button() == QtCore.Qt.RightButton:
            self.context_menu_requested.emit()
        elif self._hover_widget is not None:
            if self._hover_widget.isEnabled() and event.button() == QtCore.Qt.LeftButton:
                self.clicked.emit()
            self._hover_widget.setDown(False)
        return super().mouseReleaseEvent(event)


class _PressedIndicator(QtWidgets.QCheckBox):
    def __init__(self, name):
        super().__init__(name)
        self.setEnabled(False)

    def trigger(self):
        self.setChecked(True)
        self.setEnabled(True)
        QtCore.QTimer(self).singleShot(500, self._off)

    def _off(self):
        self.setChecked(False)
        self.setEnabled(False)


def show():
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec()


if __name__ == '__main__':
    show()
