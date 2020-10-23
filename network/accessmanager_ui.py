# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accessmanager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 254)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.url)

        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.button)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.cancel_button)

        self.progress = QProgressBar(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(24)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.progress)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delay_check = QCheckBox(self.centralwidget)
        self.delay_check.setObjectName(u"delay_check")

        self.horizontalLayout.addWidget(self.delay_check)

        self.delay_time = QDoubleSpinBox(self.centralwidget)
        self.delay_time.setObjectName(u"delay_time")
        self.delay_time.setDecimals(1)
        self.delay_time.setMinimum(0.000000000000000)
        self.delay_time.setMaximum(100.000000000000000)
        self.delay_time.setValue(0.300000000000000)

        self.horizontalLayout.addWidget(self.delay_time)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.size_label = QLabel(self.centralwidget)
        self.size_label.setObjectName(u"size_label")

        self.verticalLayout.addWidget(self.size_label)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")

        self.verticalLayout.addWidget(self.error_label)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"Get Size", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"URL to look up:", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.delay_check.setText(QCoreApplication.translate("MainWindow", u"deliberately delay", None))
        self.delay_time.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        self.size_label.setText("")
        self.error_label.setText("")
    # retranslateUi

