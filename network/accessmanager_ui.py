# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accessmanager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 167)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.url)

        self.progress = QProgressBar(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(24)

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.progress)

        self.size_label = QLabel(self.centralwidget)
        self.size_label.setObjectName(u"size_label")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.size_label)

        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.button)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.size_label.setText("")
        self.button.setText(QCoreApplication.translate("MainWindow", u"Get Size", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"URL to look up:", None))
    # retranslateUi

