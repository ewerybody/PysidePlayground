"""
Demo for a bug report on https://bugreports.qt.io/browse/PYSIDE-1744
'QLabel with markdown text hides everything past <br> linebreak'
"""

from PySide6 import QtCore, QtWidgets


TEXT = 'here comes a linebreak:<br>Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum Lorem Ipsum '


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        w = QtWidgets.QWidget(self)
        w.setMinimumSize(350, 200)
        self.setCentralWidget(w)
        self.setWindowTitle('QLabel Markdown Linebreak Demo')
        layout = QtWidgets.QFormLayout()
        w.setLayout(layout)

        for style in QtCore.Qt.PlainText, QtCore.Qt.RichText, QtCore.Qt.MarkdownText:
            group = QtWidgets.QGroupBox(str(style))
            lyt = QtWidgets.QHBoxLayout()
            group.setLayout(lyt)
            label = QtWidgets.QLabel(TEXT)
            label.setWordWrap(True)
            label.setMinimumHeight(50)
            label.setStyleSheet('background: white')
            label.setTextFormat(style)
            lyt.addWidget(label)
            layout.addWidget(group)


def show():
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec()


if __name__ == '__main__':
    show()
