import time
from PySide6 import QtWidgets, QtNetwork, QtCore, QtGui

import ui_file

DEFAULT_URL = 'https://www.qt.io'
DEFAULT_TEXT = 'nothing looked up yet'


class QNetworkAccessManagerDemo(QtWidgets.QMainWindow):
    def __init__(self):
        super(QNetworkAccessManagerDemo, self).__init__()
        self.ui = ui_file.get_module(__file__)
        self.ui.setupUi(self)
        self.ui.url.setText(DEFAULT_URL)
        self.ui.button.clicked.connect(self.lookup)
        self.ui.url.returnPressed.connect(self.lookup)
        self.ui.cancel_button.clicked.connect(self._on_cancel)
        self.setWindowTitle(self.__class__.__name__)
        self.busy_label = Spinner(self)
        self.ui.bottom_layout.insertWidget(2, self.busy_label)
        self.busy_label.hide()
        self._chunks = 0
        self._t0 = 0
        self.set_label(DEFAULT_TEXT)
        self.ui.error_label.hide()
        self.ready_ui()

        self._manager = None
        self._error_connected = False
        self._canceled = False

    def lookup(self):
        self.disable_ui()
        self.busy_label.show()
        # starting delayed to improve ux
        QtCore.QTimer(self).singleShot(200, self._lookup)

    def _lookup(self):
        url = self.ui.url.text().strip()
        if not url:
            return

        print('\nLooking up "%s" ...' % url)
        self._t0 = time.time()
        self._chunks = 0
        self._canceled = False

        if self._manager is None:
            self._manager = QtNetwork.QNetworkAccessManager(self)

        request = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        request.setRawHeader(b'User-Agent', b'MyOwnBrowser 1.0')
        reply = self._manager.get(request)
        reply.finished.connect(self._on_finish)
        reply.downloadProgress.connect(self._on_progress)
        reply.errorOccurred.connect(self._on_error)
        reply.sslErrors.connect(self._on_error)
        reply.readyRead.connect(self._on_ready_read)

        self._error_connected = False
        self._try_error_connection(reply)

    def _on_progress(self, received, total):
        if self._canceled:
            reply = self.sender()
            reply.abort()

        if received == 0 and total == 0:
            return

        if total == -1:
            prog_value = 1
        else:
            prog_value = int(100 * received / total)
        print('received/total/%%: %s %s %s%%' % (received, total, prog_value))

        self.ui.progress.setValue(prog_value)
        self._chunks += 1
        self.set_label(f'{received} bytes received in {self._chunks} chunks')
        self._visual_delay()

    def _on_finish(self):
        reply = self.sender()

        data = reply.readAll().data()
        try:
            print(f'data: {data[:256].decode()}\n...')
        except UnicodeDecodeError:
            print(f'data: {data[:256].decode("latin1")}\n...')

        self.append_label(f' <i> - in {time.time() - self._t0:.2f} seconds.</i>')
        self._visual_delay()
        self.ready_ui()

    def _on_ready_read(self):
        # currently doing nothing ...
        reply = self.sender()
        thread = reply.thread()
        print(f'_on_ready_read size: {reply.size()}')
        self._try_error_connection(reply)

    def set_label(self, text):
        self.ui.size_label.setText(text)

    def append_label(self, text):
        self.set_label(self.ui.size_label.text() + text)

    def ready_ui(self, *stuff):
        self.ui.progress.hide()
        self.busy_label.hide()
        self.ui.cancel_button.hide()
        for widget in (self.ui.button, self.ui.url):
            widget.setEnabled(True)
            widget.blockSignals(False)
        self.ui.url.setFocus()

    def disable_ui(self):
        self.ui.error_label.hide()
        self.ui.error_label.setText('')
        self.set_label(DEFAULT_TEXT)
        for widget in (self.ui.button, self.ui.url):
            widget.setEnabled(False)
            widget.blockSignals(True)
        self.ui.progress.setValue(0)
        self.ui.cancel_button.show()
        self.ui.progress.show()

    def _on_error(self, error):
        """A thrown error does not mean its finished. There might be more!"""
        self.ui.error_label.show()
        reply = self.sender()
        msg = f'<b>Error</b>: {error.name.decode()}<br><b>errorString</b>: {reply.errorString()}'
        current = self.ui.error_label.text()
        if not current:
            self.ui.error_label.setText(msg)
        elif current != msg:
            self.ui.error_label.setText(f'{current}<br>{msg}')
            print(f'Error thrown: {error.name.decode()}\n  {reply.errorString()}')
        else:
            # Label is already set. Nothing to do.
            pass

    def _visual_delay(self):
        if self.ui.delay_check.isChecked():
            QtWidgets.QApplication.instance().processEvents()
            time.sleep(self.ui.delay_time.value())

    def _try_error_connection(self, reply):
        """
        Hmm. Seems we're unable to connect to a "errorOccured" while in flight.
        As soon as we debug the signal is there and connectable ... weird.
        The "error" one works tho!
        """
        if self._error_connected:
            return

        for signal_name in ('error', 'errorOccured'):
            if not hasattr(reply, signal_name):
                continue
            signal = getattr(reply, signal_name)
            try:
                signal.connect(self._on_error)
                self._error_connected = True
                print(f'Connected to error signal: "{signal_name}"')
            except AttributeError:
                # print('Weird. No "errorOccured" Signal yet...')
                self._error_connected = False

    def _on_cancel(self):
        self._canceled = True


class Spinner(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Spinner, self).__init__(parent)
        import os
        THIS_DIR = os.path.abspath(os.path.dirname(__file__))
        self._pixmap_resource = QtGui.QPixmap(os.path.join(THIS_DIR, 'spinner.svg'))
        self._pixmaps = {}
        self._speed = 20
        self._rotation = 0
        self._size = 32

        self.update_timer = QtCore.QTimer(self)
        self.update_timer.setInterval(30)
        self.update_timer.timeout.connect(self._update)

    def show(self):
        self.update_timer.start()
        super(Spinner, self).show()

    def hide(self):
        self.update_timer.stop()
        self._rotation = 0
        super(Spinner, self).hide()

    def _update(self):
        self._rotation = (self._rotation + self._speed) % 360
        this_pixmap = self._pixmaps.get(self._rotation)
        if this_pixmap is None:
            this_pixmap = self._pixmap_resource.transformed(
                QtGui.QTransform().rotate(self._rotation),
                QtCore.Qt.SmoothTransformation
            )
            xoff = (this_pixmap.width() - self._size) / 2
            yoff = (this_pixmap.height() - self._size) / 2
            this_pixmap = this_pixmap.copy(xoff, yoff, self._size, self._size)
            self._pixmaps[self._rotation] = this_pixmap
        self.setPixmap(this_pixmap)


def main():
    app = QtWidgets.QApplication([])
    win = QNetworkAccessManagerDemo()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()
