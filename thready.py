import uuid
from PySide2 import QtWidgets, QtCore


class SimpleThreadDemo(QtWidgets.QMainWindow):
    def __init__(self):
        super(SimpleThreadDemo, self).__init__()
        self.setWindowTitle(self.__class__.__name__)

        widget = QtWidgets.QWidget(self)
        self.setCentralWidget(widget)
        layout = QtWidgets.QVBoxLayout(widget)
        button = QtWidgets.QPushButton('Stop')
        layout.addWidget(button)
        line_edit = QtWidgets.QLineEdit()
        layout.addWidget(line_edit)

        self.thread = GarbageThrower(self)
        self.thread.garbage.connect(line_edit.setText)
        self.thread.finished.connect(self.thread.deleteLater)
        button.clicked.connect(self.thread.stop)
        self.thread.start()

    def closeEvent(self, event):
        if not self.thread._stopped:
            self.thread.stop()
            while self.thread.isRunning():
                pass
        return super(SimpleThreadDemo, self).closeEvent(event)


class GarbageThrower(QtCore.QThread):
    garbage = QtCore.Signal(str)

    def __init__(self, parent):
        super(GarbageThrower, self).__init__(parent)
        self._stopped = False

    def stop(self):
        self._stopped = True

    def run(self):
        while not self._stopped:
            self.garbage.emit(str(uuid.uuid4()))
            self.msleep(100)
        self.garbage.emit('self._stopped: %s' % self._stopped)


def main():
    app = QtWidgets.QApplication([])
    win = SimpleThreadDemo()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
