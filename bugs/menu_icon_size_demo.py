from PySide6 import QtCore, QtWidgets, QtGui


STYLE_1 = 'QMenu {{icon-size: {size}px;}}'
STYLE_2 = 'QMenu::item {{background: transparent;}}'
STYLE_3 = 'QMenu::item:selected {{icon-size: {size}px;}}'

MIN_SIZE = 12
MAX_SIZE = 128
DEFAULT_SIZE = 24

MSG_SEL_HIDDEN = 'Selection Hides item text.'
MSG_SIZE_IGNORED = 'Icon size ignored.'
MSG_SPACE = 'Space for icon set.'
MSG_SIZE_SET = 'Icon size set!'
MSG_SEL_BG = 'Selection background set.'
MSG_SIZE_SEL = 'Size set only on selected.'
LABELS = {
    '000': MSG_SIZE_IGNORED,
    '001': MSG_SIZE_IGNORED + MSG_SEL_BG,
    '010': MSG_SIZE_IGNORED + MSG_SEL_HIDDEN,
    '011': MSG_SIZE_IGNORED + MSG_SEL_BG,
    '100': MSG_SIZE_IGNORED + MSG_SPACE,
    '101': MSG_SIZE_SEL,
    '110': MSG_SIZE_SET + MSG_SEL_HIDDEN,
    '111': MSG_SIZE_SET,
}

class MenuIconSizeDemo(QtWidgets.QWidget):
    def __init__(self):
        super(MenuIconSizeDemo, self).__init__()
        self._size = DEFAULT_SIZE
        self.setWindowTitle('MenuIconSizeDemo')
        self.setWindowIcon(self._get_icon())
        layout = QtWidgets.QVBoxLayout(self)

        self._checks = []
        for line in STYLE_1, STYLE_2, STYLE_3:
            check = QtWidgets.QCheckBox(line)
            self._checks.append(check)
            layout.addWidget(check)
            check.setChecked(True)
            check.clicked[bool].connect(self._set_style)

        self.label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button1.setText('Click Me!')
        layout.addWidget(self.button1)
        self.button_menu1 = QtWidgets.QMenu(self.button1)


        hlayout = QtWidgets.QHBoxLayout()
        self.slider = QtWidgets.QSlider(self)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.spinbox = QtWidgets.QSpinBox()

        for x in self.spinbox, self.slider:
            x.setValue(self._size)
            x.setMinimum(MIN_SIZE)
            x.setMaximum(MAX_SIZE)
            x.valueChanged.connect(self._size_value_changed)
            hlayout.addWidget(x)
        layout.addLayout(hlayout)

        self._set_style()

    def on_button1_clicked(self):
        self.button_menu1.clear()
        for i in range(3):
            self.button_menu1.addAction(self._get_icon(), 'Hello %i!' % (i + 1))
        self.button_menu1.popup(QtGui.QCursor.pos())

    def _size_value_changed(self):
        widget = self.sender()
        self._size = widget.value()
        self._set_style()

        for x in self.slider, self.spinbox:
            if x is not widget:
                x.blockSignals(True)
                x.setValue(self._size)
                x.blockSignals(False)
                return

    def _set_style(self):
        style = ''
        check_pattern = ''
        for check in self._checks:
            check_pattern += str(int(check.isChecked()))
            if not check.isChecked():
                continue
            style += check.text()
        print('check_pattern: %s' % check_pattern)
        self.button_menu1.setStyleSheet(style.format(size=self._size))
        self.label.setText(LABELS[check_pattern])


    def _get_icon(self):
        pixmap = QtGui.QPixmap(self._size, self._size)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        color = QtCore.Qt.green
        brush = QtGui.QBrush(color)
        painter.setBrush(brush)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawEllipse(0, 0, self._size, self._size)
        painter.end()
        return QtGui.QIcon(pixmap)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = MenuIconSizeDemo()
    main.show()
    app.exec()
