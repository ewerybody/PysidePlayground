"""
Created with some help from the Qt for Python telegram channel! Thanks!
"""
from PySide6 import QtCore, QtGui, QtWidgets


class BuiltInIconsExample(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QtWidgets.QVBoxLayout(self)

        dit = QtCore.QDirIterator(':', QtCore.QDirIterator.Subdirectories)
        collect = ('png', 'svg', 'ico')
        things = {}
        while dit.hasNext():
            fnfo = dit.fileInfo()
            if fnfo.isFile() and fnfo.suffix() in collect:
                pth = dit.filePath()
                things.setdefault(pth.strip(':/').split('/', 1)[0], []).append(pth)
            dit.next()

        rlist = QtWidgets.QListWidget(self)
        rlist.setMinimumSize(800, 600)
        rlist.setViewMode(QtWidgets.QListWidget.IconMode)
        rlist.setSpacing(0)
        rlist.setResizeMode(QtWidgets.QListWidget.Adjust)
        rlist.setUniformItemSizes(True)

        value = 128
        size = QtCore.QSize(value, value)
        rlist.setIconSize(size)
        rlist.setGridSize(size)
        self.main_layout.addWidget(rlist)
        
        # It used to be 'trolltech' in PySide1 ... Yeah I tested the code with that version.
        for project_name in 'qt-project.org', 'trolltech':
            if project_name not in things:
                continue
            for path in sorted(things.get(project_name, '')):
                item = QtWidgets.QListWidgetItem()
                item.setToolTip(path)
                icon = QtGui.QIcon(path)
                item.setIcon(icon)
                item.setSizeHint(size)
                rlist.addItem(item)
            break


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = BuiltInIconsExample()
    main.show()
    app.exec()
