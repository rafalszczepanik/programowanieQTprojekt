# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

import ui as ui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class FirstSite(object):
    def setupUi(self, Form):
        Form.setObjectName("KALKULATOR FIGUR PŁASKICH")
        Form.resize(578, 557)
        self.kwadratBUTTON = QtWidgets.QPushButton(Form)
        self.kwadratBUTTON.setGeometry(QtCore.QRect(30, 70, 151, 101))
        self.kwadratBUTTON.setObjectName("kwadratBUTTON")
        self.koloBUTTON = QtWidgets.QPushButton(Form)
        self.koloBUTTON.setGeometry(QtCore.QRect(220, 70, 151, 101))
        self.koloBUTTON.setObjectName("koloBUTTON")
        self.prostokatBUTTON = QtWidgets.QPushButton(Form)
        self.prostokatBUTTON.setGeometry(QtCore.QRect(410, 70, 151, 101))
        self.prostokatBUTTON.setObjectName("prostokatBUTTON")
        self.rownoleglobokBUTTON = QtWidgets.QPushButton(Form)
        self.rownoleglobokBUTTON.setGeometry(QtCore.QRect(410, 230, 151, 101))
        self.rownoleglobokBUTTON.setObjectName("rownoleglobokBUTTON")
        self.trojkatBUTTON = QtWidgets.QPushButton(Form)
        self.trojkatBUTTON.setGeometry(QtCore.QRect(30, 230, 151, 101))
        self.trojkatBUTTON.setObjectName("trojkatBUTTON")
        self.rombBUTTON = QtWidgets.QPushButton(Form)
        self.rombBUTTON.setGeometry(QtCore.QRect(220, 230, 151, 101))
        self.rombBUTTON.setObjectName("rombBUTTON")
        self.exitBUTTON = QtWidgets.QPushButton(Form)
        self.exitBUTTON.setGeometry(QtCore.QRect(410, 470, 141, 31))
        self.exitBUTTON.setObjectName("exitBUTTON")
        self.trapezBUTTON = QtWidgets.QPushButton(Form)
        self.trapezBUTTON.setGeometry(QtCore.QRect(30, 400, 151, 101))
        self.trapezBUTTON.setObjectName("trapezBUTTON")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 400, 151, 101))
        self.pushButton_9.setObjectName("pushButton_9")
        #self.lineEdit = QtWidgets.QLineEdit(Form)
       # self.lineEdit.setGeometry(QtCore.QRect(80, 10, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
       # self.lineEdit.setFont(font)
       # self.lineEdit.setObjectName("lineEdit")
        self.helpButton = QtWidgets.QPushButton(Form)
        self.helpButton.setGeometry(QtCore.QRect(410, 400, 141, 31))
        self.helpButton.setObjectName("helpButton")

        self.retranslateUi(Form)
        
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KALKULATOR FIGUR PŁASKICH"))
        self.kwadratBUTTON.setText(_translate("Form", "KWADRAT"))
        self.koloBUTTON.setText(_translate("Form", "KOŁO"))
        self.prostokatBUTTON.setText(_translate("Form", "PROSTOKĄT"))
        self.rownoleglobokBUTTON.setText(_translate("Form", "RÓWNOLEGŁOBOK"))
        self.trojkatBUTTON.setText(_translate("Form", "TRÓJKĄT"))
        self.rombBUTTON.setText(_translate("Form", "ROMB"))
        self.exitBUTTON.setText(_translate("Form", "EXIT"))
        self.trapezBUTTON.setText(_translate("Form", "TRAPEZ"))
        self.pushButton_9.setText(_translate("Form", "DELTOID"))
        #self.lineEdit.setText(_translate("Form", "Kalkulator Figur Płaskich"))
        self.helpButton.setText(_translate("Form", "HELP"))



