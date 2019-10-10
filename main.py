# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 368)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.vertCommands = QtWidgets.QVBoxLayout()
        self.vertCommands.setObjectName("vertCommands")
        self.commandMode = QtWidgets.QPushButton(Form)
        self.commandMode.setObjectName("commandMode")
        self.vertCommands.addWidget(self.commandMode)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.takeoff = QtWidgets.QPushButton(Form)
        self.takeoff.setObjectName("takeoff")
        self.horizontalLayout_2.addWidget(self.takeoff)
        self.land = QtWidgets.QPushButton(Form)
        self.land.setObjectName("land")
        self.horizontalLayout_2.addWidget(self.land)
        self.vertCommands.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.vertCommands)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.vertText = QtWidgets.QVBoxLayout()
        self.vertText.setObjectName("vertText")
        self.emergency = QtWidgets.QPushButton(Form)
        self.emergency.setObjectName("emergency")
        self.vertText.addWidget(self.emergency)
        self.commandText = QtWidgets.QTextBrowser(Form)
        self.commandText.setObjectName("commandText")
        self.vertText.addWidget(self.commandText)
        self.horizontalLayout.addLayout(self.vertText)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.commandMode.setText(_translate("Form", "Enable Commands"))
        self.takeoff.setText(_translate("Form", "Takeoff"))
        self.land.setText(_translate("Form", "Land"))
        self.emergency.setText(_translate("Form", "EMERGENCY"))
