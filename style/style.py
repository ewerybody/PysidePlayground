import os
import sys

from PySide6.QtWidgets import QApplication, QCheckBox

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(THIS_DIR, 'style.qss')) as fobj:
    c_style = fobj.read()

app = QApplication()

c = QCheckBox("option")
c.setStyleSheet(c_style)
# c.setFixedSize(200, 100)
c.show()

sys.exit(app.exec_())
