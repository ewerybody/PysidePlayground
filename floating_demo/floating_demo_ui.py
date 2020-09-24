# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'floating_demo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(814, 441)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.layout_0 = QVBoxLayout()
        self.layout_0.setObjectName(u"layout_0")
        self.layout_0.setContentsMargins(-1, 0, -1, -1)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 472, 481))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.layout_0.addWidget(self.scrollArea)


        self.gridLayout.addLayout(self.layout_0, 0, 0, 1, 1)

        self.layout_1 = QHBoxLayout()
        self.layout_1.setContentsMargins(40, 40, 40, 40)
        self.layout_1.setObjectName(u"layout_1")
        self.button_left = QPushButton(Form)
        self.button_left.setObjectName(u"button_left")
        self.button_left.setMinimumSize(QSize(100, 50))
        self.button_left.setMaximumSize(QSize(50, 50))

        self.layout_1.addWidget(self.button_left)

        self.button_right = QPushButton(Form)
        self.button_right.setObjectName(u"button_right")
        self.button_right.setMinimumSize(QSize(100, 50))
        self.button_right.setMaximumSize(QSize(50, 50))

        self.layout_1.addWidget(self.button_right)


        self.gridLayout.addLayout(self.layout_1, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, Te"
                        "xtLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, ", None))
        self.button_left.setText(QCoreApplication.translate("Form", u"<", None))
        self.button_right.setText(QCoreApplication.translate("Form", u">", None))
    # retranslateUi

