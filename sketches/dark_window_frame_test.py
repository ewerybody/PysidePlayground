import sys
import winreg

from PySide6 import QtCore, QtWidgets

PERSONALIZE_KEY = r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize'


class Demo(QtWidgets.QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle(self.__class__.__name__)
        self.setMinimumSize(300, 200)
        layout = QtWidgets.QVBoxLayout(self)
        # layout.addWidget()


if __name__ == '__main__':
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, PERSONALIZE_KEY) as reg_key:
        use_light_theme = winreg.QueryValueEx(reg_key, 'AppsUseLightTheme')[0]
    print('use_light_theme: %s' % use_light_theme)
    sys.argv.extend(('-platform', 'windows:darkmode=0'))
    # sys.argv.extend(('-platform', 'windows:darkmode=1'))
    app = QtWidgets.QApplication(sys.argv)
    main = Demo()
    main.show()
    app.exec()
