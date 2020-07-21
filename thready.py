"""
An attempt in most proper QThread usage.
* cares for the thread to finish naturally
* cares for it to finish on window close
* also when it has finished before already
"""
import time
import uuid

import shiboken2
from PySide2 import QtWidgets, QtCore


class SimpleThreadDemo(QtWidgets.QMainWindow):
    def __init__(self):
        super(SimpleThreadDemo, self).__init__()
        self.setWindowTitle(self.__class__.__name__)
        widget = QtWidgets.QWidget(self)
        self.setMinimumWidth(350)
        self.setCentralWidget(widget)

        # just stack a button and a line edit
        layout = QtWidgets.QVBoxLayout(widget)
        button = QtWidgets.QPushButton('Stop')
        line_edit = QtWidgets.QLineEdit()
        layout.addWidget(button)
        layout.addWidget(line_edit)

        # build the thread, connect its message signal to the line edit
        self.thread = GarbageThrower(self)
        self.thread.garbage.connect(line_edit.setText)
        self.thread.finished.connect(self.thread.deleteLater)
        # connect the button to requestInterruption and start it
        button.clicked.connect(self.thread.requestInterruption)
        self.thread.start()

    def closeEvent(self, event):
        """
        Make sure all is shut down properly.

        With `shiboken2.isValid` we can avoid try/excepting this
          RuntimeError: Internal C++ object already deleted.
        which would be inevitable without further book keeping.
        """
        if shiboken2.isValid(self.thread):
            # If not interrupted already, request and wait as long as it takes.
            self.thread.requestInterruption()
            while self.thread.isRunning():
                time.sleep(0.05)

        return super(SimpleThreadDemo, self).closeEvent(event)


class GarbageThrower(QtCore.QThread):
    garbage = QtCore.Signal(str)

    def run(self):
        while not self.isInterruptionRequested():
            self.garbage.emit(str(uuid.uuid4()))
            self.msleep(100)
        self.garbage.emit('self.isInterruptionRequested: %s' % self.isInterruptionRequested())


def main():
    app = QtWidgets.QApplication([])
    win = SimpleThreadDemo()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
