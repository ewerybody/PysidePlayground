"""Is that a bug? At lease this illustrates an inconsistency
between `QListWidget` and `QTreeWidget`s function `setCurrentItem`.
"""
from PySide2 import QtCore, QtWidgets

ITEMS = 'mango banana apple kiwi apple strawberry'.split()

class Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        w = QtWidgets.QWidget(self)
        self.setCentralWidget(w)
        hlyt = QtWidgets.QHBoxLayout(w)

        vlyt = QtWidgets.QVBoxLayout()
        vlyt.addWidget(QtWidgets.QLabel('<b>QListWidget</b>'))
        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.addItems(ITEMS)
        self.list_widget.setSelectionMode(self.list_widget.SelectionMode.ExtendedSelection)
        vlyt.addWidget(self.list_widget)
        button = QtWidgets.QPushButton('Select items and set current')
        button.clicked.connect(self.select_list)
        vlyt.addWidget(button)
        hlyt.addLayout(vlyt)

        vlyt = QtWidgets.QVBoxLayout()
        vlyt.addWidget(QtWidgets.QLabel('<b>QTreeWidget</b>'))
        self.tree_widget = QtWidgets.QTreeWidget(self)
        self.tree_widget.header().setVisible(False)
        self.tree_widget.setIndentation(0)
        for name in ITEMS:
            QtWidgets.QTreeWidgetItem(self.tree_widget, [name])
        self.tree_widget.setSelectionMode(self.tree_widget.SelectionMode.ExtendedSelection)
        button = QtWidgets.QPushButton('Select items and set current')
        button.clicked.connect(self.select_tree)
        vlyt.addWidget(self.tree_widget)
        vlyt.addWidget(button)
        self.sel_flag_check = QtWidgets.QCheckBox('Pass SelectionFlag.Current')
        vlyt.addWidget(self.sel_flag_check)
        hlyt.addLayout(vlyt)

    def select_list(self):
        items = [self.list_widget.item(i) for i in range(self.list_widget.count())]
        self.list_widget.clearSelection()
        for item in items[2:5]:
            item.setSelected(True)
        self.list_widget.setCurrentItem(items[4])

    def select_tree(self):
        items = [self.tree_widget.topLevelItem(i) for i in range(self.tree_widget.topLevelItemCount())]
        self.tree_widget.clearSelection()
        for item in items[2:5]:
            item.setSelected(True)
        if self.sel_flag_check.isChecked():
            self.tree_widget.setCurrentItem(items[4], 0, QtCore.QItemSelectionModel.Current)
        else:
            self.tree_widget.setCurrentItem(items[4])


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = Demo()
    win.show()
    app.exec_()
