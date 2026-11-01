################################################################################
## Form generated from reading UI file 'floating_demo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Form:
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName('Form')
        Form.resize(814, 441)
        Form.setWindowTitle('Form')
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName('gridLayout')
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMinimumSize
        )
        self.layout_0 = QtWidgets.QVBoxLayout()
        self.layout_0.setObjectName('layout_0')
        self.layout_0.setContentsMargins(-1, 0, -1, -1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setObjectName('scrollArea')
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContents')
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 472, 481))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName('label')
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.layout_0.addWidget(self.scrollArea)

        self.gridLayout.addLayout(self.layout_0, 0, 0, 1, 1)

        self.layout_1 = QtWidgets.QHBoxLayout()
        self.layout_1.setObjectName('layout_1')
        self.layout_1.setContentsMargins(40, 40, 40, 40)
        self.button_left = QtWidgets.QPushButton(Form)
        self.button_left.setObjectName('button_left')
        self.button_left.setMinimumSize(QtCore.QSize(100, 50))
        self.button_left.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Light)
        self.button_left.setFont(font)

        self.layout_1.addWidget(self.button_left)

        self.button_right = QtWidgets.QPushButton(Form)
        self.button_right.setObjectName('button_right')
        self.button_right.setMinimumSize(QtCore.QSize(100, 50))
        self.button_right.setMaximumSize(QtCore.QSize(50, 50))
        self.button_right.setFont(font)

        self.layout_1.addWidget(self.button_right)

        self.gridLayout.addLayout(self.layout_1, 0, 1, 1, 1)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.label.setText(
            QtCore.QCoreApplication.translate(
                'Form',
                'TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, Te'
                'xtLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, TextLabel, ',
                None,
            )
        )
        self.button_left.setText(QtCore.QCoreApplication.translate('Form', '<', None))
        self.button_right.setText(QtCore.QCoreApplication.translate('Form', '>', None))
