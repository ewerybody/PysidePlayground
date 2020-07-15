import time
from PySide2 import QtWidgets, QtNetwork, QtCore

import ui_file

DEFAULT_URL = 'https://www.qt.io'
DEFAULT_TOTAL = 100000
DEFAULT_TEXT = 'nothing looked up yet'


class QNetworkAccessManagerDemo(QtWidgets.QMainWindow):
    def __init__(self):
        super(QNetworkAccessManagerDemo, self).__init__()
        self.ui = ui_file.get_module(__file__)
        self.ui.setupUi(self)
        self.ui.url.setText(DEFAULT_URL)
        self.ui.button.clicked.connect(self.lookup)
        self._chunks = 0
        self._t0 = 0
        self.set_label(DEFAULT_TEXT)
        self.ready_ui()

    def lookup(self):
        self.disable_ui()
        QtCore.QTimer(self).singleShot(200, self._lookup)

    def _lookup(self):
        url = self.ui.url.text().strip()
        if not url:
            return

        self._t0 = time.time()
        self._chunks = 0
        manager = QtNetwork.QNetworkAccessManager(self)
        # manager.finished[QtNetwork.QNetworkReply].connect(self._on_finish)
        request = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        request.setRawHeader(b'User-Agent', b'MyOwnBrowser 1.0')
        reply = manager.get(request)
        reply.finished.connect(self._on_finish)
        reply.downloadProgress.connect(self._on_progress)
        reply.error[QtNetwork.QNetworkReply.NetworkError].connect(self._on_error)
        reply.sslErrors.connect(self._on_error)
        # reply.errorOccured.connect(self._on_error)
        reply.readyRead.connect(self._on_ready_read)

    def _on_ready_read(self, *stuff):
        stuff
        sender = self.sender()
        sender

    def _on_progress(self, received, total):
        if received == 0 and total == 0:
            return
        if total == -1:
            total = DEFAULT_TOTAL
        self.ui.progress.setValue(int(received/total))
        self._chunks += 1
        self.set_label(f'{received} bytes received in {self._chunks} chunks')

    def _on_error(self, error):
        self.set_label(f'Error: {error.name.decode()}')
        self.ready_ui()

    def _on_finish(self):
        reply = self.sender()
        # error = reply.errorString()
        # if error:
        #     self.set_label(f'Error: {error}')
        # else:
        self.append_label(f' in {time.time() - self._t0:.2f} seconds.')
        self.ready_ui()

    def set_label(self, text):
        self.ui.size_label.setText(text)

    def append_label(self, text):
        self.set_label(self.ui.size_label.text() + text)

    def ready_ui(self, *stuff):
        self.ui.progress.hide()
        for widget in (self.ui.button, self.ui.url):
            widget.setEnabled(True)

    def disable_ui(self):
        self.set_label(DEFAULT_TEXT)
        for widget in (self.ui.button, self.ui.url):
            widget.setEnabled(False)
        self.ui.progress.setValue(0)
        self.ui.progress.show()


def main():
    app = QtWidgets.QApplication([])
    win = QNetworkAccessManagerDemo()
    win.show()
    app.exec_()

if __name__ == "__main__":
    main()
