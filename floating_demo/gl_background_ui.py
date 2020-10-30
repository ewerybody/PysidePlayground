# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gl_background.ui'
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
        Form.resize(1143, 714)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.layout_0 = QVBoxLayout()
        self.layout_0.setObjectName(u"layout_0")
        self.layout_0.setContentsMargins(-1, 0, -1, -1)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scroller_widget = QWidget()
        self.scroller_widget.setObjectName(u"scroller_widget")
        self.scroller_widget.setGeometry(QRect(0, 0, 629, 710))
        self.scroller_layout = QVBoxLayout(self.scroller_widget)
        self.scroller_layout.setContentsMargins(0, 0, 0, 0)
        self.scroller_layout.setObjectName(u"scroller_layout")
        self.scrollArea.setWidget(self.scroller_widget)

        self.layout_0.addWidget(self.scrollArea)


        self.gridLayout.addLayout(self.layout_0, 0, 0, 1, 1)

        self.layout_1 = QVBoxLayout()
        self.layout_1.setContentsMargins(40, 40, 40, 40)
        self.layout_1.setObjectName(u"layout_1")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 100, -1, 100)
        self.button_left = QPushButton(Form)
        self.button_left.setObjectName(u"button_left")
        self.button_left.setMinimumSize(QSize(100, 50))
        self.button_left.setMaximumSize(QSize(50, 50))
        self.button_left.setFlat(False)

        self.horizontalLayout.addWidget(self.button_left)

        self.button_right = QPushButton(Form)
        self.button_right.setObjectName(u"button_right")
        self.button_right.setMinimumSize(QSize(100, 50))
        self.button_right.setMaximumSize(QSize(50, 50))
        self.button_right.setFlat(False)

        self.horizontalLayout.addWidget(self.button_right)


        self.layout_1.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: white;")
        self.label_2.setWordWrap(True)

        self.layout_1.addWidget(self.label_2)


        self.gridLayout.addLayout(self.layout_1, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_left.setText(QCoreApplication.translate("Form", u"<", None))
        self.button_right.setText(QCoreApplication.translate("Form", u">", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel", None))
    # retranslateUi

