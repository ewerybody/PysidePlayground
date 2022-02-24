"""
This used to delete multipe items for no apparent reasons.
Seems fixed now!
"""

from PySide6 import QtGui, QtCore, QtWidgets

if QtCore.__version_info__[0] > 5:
    from PySide6.QtGui import QShortcut
else:
    from PySide2.QtWidgets import QShortcut


class AList(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(AList, self).__init__(parent)

        # BAD: inline - twiggers twice
        QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete), self, self.remove_selected)

        # Good: twiggers once
        shortcut = QShortcut(self)
        shortcut.setKey(QtGui.QKeySequence(QtCore.Qt.Key_D))
        shortcut.activated.connect(self.remove_selected)

    def remove_selected(self):
        if sel := self.selectedItems():
            print(f'{len(sel)} items selected ...')
            for item in sel:
                print(f'Removing {item.text()} ...')
                idx = self.indexFromItem(item)
                self.takeItem(idx.row())
        else:
            print('Noting items selected')


class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        w = QtWidgets.QWidget(self)
        self.setCentralWidget(w)
        lyt = QtWidgets.QVBoxLayout(w)
        w.setLayout(lyt)

        lyt.addWidget(QtWidgets.QLabel('Delete a thing with the <b>Del</b> key:'))
        self.widget1 = AList(self)
        self.widget1.addItems('mango banana apple kiwi apple strawberry'.split())
        lyt.addWidget(self.widget1)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec_()
