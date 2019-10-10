# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Connect(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(175, 86)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Connect.sizePolicy().hasHeightForWidth())
        Connect.setSizePolicy(sizePolicy)
        Connect.setMaximumSize(QtCore.QSize(175, 86))
        self.verticalLayout = QtWidgets.QVBoxLayout(Connect)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Connect)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ip = QtWidgets.QLineEdit(Connect)
        self.ip.setObjectName("ip")
        self.verticalLayout.addWidget(self.ip)
        self.connect = QtWidgets.QPushButton(Connect)
        self.connect.setObjectName("connect")
        self.verticalLayout.addWidget(self.connect)

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("Connect", "Connect to Tello"))
        self.label.setText(_translate("Connect", "Enter the IP Address of the Tello"))
        self.connect.setText(_translate("Connect", "Connect"))
