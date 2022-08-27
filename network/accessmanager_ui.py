# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accessmanager.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 254)
        MainWindow.setWindowTitle(u"MainWindow")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"URL to look up:")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.url = QLineEdit(self.centralwidget)
        self.url.setObjectName(u"url")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.url)

        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setText(u"Get Size")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.button)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.size_label = QLabel(self.centralwidget)
        self.size_label.setObjectName(u"size_label")
        self.size_label.setText(u"")

        self.verticalLayout_2.addWidget(self.size_label)

        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setText(u"")

        self.verticalLayout_2.addWidget(self.error_label)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.verticalLayout_2)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setText(u"Cancel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.cancel_button)

        self.progress = QProgressBar(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(24)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.progress)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.delay_check = QCheckBox(self.centralwidget)
        self.delay_check.setObjectName(u"delay_check")
        self.delay_check.setText(u"deliberately delay")

        self.bottom_layout.addWidget(self.delay_check)

        self.delay_time = QDoubleSpinBox(self.centralwidget)
        self.delay_time.setObjectName(u"delay_time")
        self.delay_time.setDecimals(1)
        self.delay_time.setMinimum(0.000000000000000)
        self.delay_time.setMaximum(100.000000000000000)
        self.delay_time.setValue(0.300000000000000)

        self.bottom_layout.addWidget(self.delay_time)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottom_layout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.bottom_layout)

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
        self.delay_time.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
        pass
    # retranslateUi

