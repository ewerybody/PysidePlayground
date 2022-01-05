"""
An attempt in most proper QThread usage.
* cares for the thread to finish naturally
* cares for it to finish on window close
* also when it has finished before already
"""
import time
import uuid

import shiboken6
from PySide6 import QtWidgets, QtCore


class SimpleThreadDemo(QtWidgets.QMainWindow):
    def __init__(self):
        super(SimpleThreadDemo, self).__init__()
        self.setWindowTitle(self.__class__.__name__)
        widget = QtWidgets.QWidget(self)
        self.setMinimumWidth(350)
        self.setCentralWidget(widget)

        # just stack a button and a line edit
        layout = QtWidgets.QVBoxLayout(widget)
        self.button = QtWidgets.QPushButton()
        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.button)
        layout.addWidget(self.line_edit)
        self.button.clicked.connect(self.toggle_thread)

        self.thread = None
        self.start()

    def start(self):
        """
        Build the thread, connect its message signals and start it.
        """
        # Pass `self` so the thread can parent to!
        self.thread = GarbageThrower(self)
        self.thread.garbage.connect(self.line_edit.setText)
        self.thread.finished.connect(self.stopped)
        self.thread.start()
        self.button.setText('Stop')

    def stop(self):
        if self.thread is None:
            return
        self.thread.requestInterruption()

    def stopped(self):
        thread = self.sender()
        thread.deleteLater()
        self.thread = None
        self.button.setText('Start')

    def toggle_thread(self):
        if self.thread is None:
            self.start()
        else:
            self.stop()

    def closeEvent(self, event):
        """
        Make sure all is shut down properly.

        With `shiboken2.isValid` we can avoid try/excepting this
          RuntimeError: Internal C++ object already deleted.
        which would be inevitable without further book keeping.
        """
        if shiboken2.isValid(self.thread) and self.thread is not None:
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
        # run() is exiting here and the finished signal will be emitted.


def main():
    app = QtWidgets.QApplication([])
    win = SimpleThreadDemo()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()
