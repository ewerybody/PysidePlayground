import random
import time

from PySide6 import QtCore, QtWidgets

MAX_LOOPS = 256
MAX_TIME = 1
CHUNK_SIZE = 2 ** 10


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QVBoxLayout(self)
        self.button = QtWidgets.QPushButton(self)
        self.button.setObjectName('button')
        self.button.setText('TEST')
        # self.field = QtWidgets.QTextEdit()
        # self.field_set_func = self.field.setText
        self.field = QtWidgets.QPlainTextEdit()
        self.field_set_func = self.field.setPlainText
        layout.addWidget(self.field)
        layout.addWidget(self.button)

        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.Slot()
    def on_button_clicked(self):
        t1 = 0
        count = 1
        while t1 < MAX_TIME and count < MAX_LOOPS:
            t0 = time.time()
            num_chars = CHUNK_SIZE * count
            print(f'{num_chars = }')
            t00 = time.time()
            rnd = ''.join(randc() for _ in range(num_chars))
            print(f'     {"rnd"} took {(time.time() - t00):.3f}s')
            count += 1

            t00 = time.time()
            self.field.clear()
            print('     {} took {:.3f}s'.format('clear', time.time() - t00))

            t00 = time.time()
            self.field_set_func(f'{num_chars} {rnd}')
            print('     {} took {:.3f}s'.format('setText', time.time() - t00))

            t00 = time.time()
            QtWidgets.QApplication.processEvents()
            print('     {} took {:.3f}s'.format('processEvents', time.time() - t00))

            t1 = time.time() - t0
        print(f'{count = }')
        print(f'{t1 = }')


def randc():
    return chr(random.randint(65, 65 + 26 - 1) + 32 * random.randint(0, 1))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main = Widget()
    main.show()
    app.exec()
