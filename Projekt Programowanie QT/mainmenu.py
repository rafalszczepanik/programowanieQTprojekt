# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from kwadrat import Ui_Kwadrat
from kolo import Ui_Kolo
from prostokat import Ui_Prostokat


class FirstSite(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def setupUi(self, Form):
        Form.setObjectName("Kalkulator figur płaskich")
        Form.resize(578, 557)
        Form.setStyleSheet("background:rgb(255, 225, 255)")
        self.KwadratButton = QtWidgets.QPushButton(Form)
        self.KwadratButton.setEnabled(True)
        self.KwadratButton.setGeometry(QtCore.QRect(20, 70, 151, 101))
        self.KwadratButton.setMouseTracking(False)
        self.KwadratButton.setTabletTracking(False)
        self.KwadratButton.setAcceptDrops(False)
        self.KwadratButton.setAutoFillBackground(False)
        self.KwadratButton.setStyleSheet("background:rgb(0, 153, 255)\n"
                                         "QPuschButton(color: black)\n"
                                         "\n"
                                         "")
        self.KwadratButton.setCheckable(False)
        self.KwadratButton.setAutoRepeat(False)
        self.KwadratButton.setAutoDefault(False)
        self.KwadratButton.setDefault(False)
        self.KwadratButton.setFlat(False)
        self.KwadratButton.setObjectName("KwadratButton")
        self.koloBUTTON = QtWidgets.QPushButton(Form)
        self.koloBUTTON.setGeometry(QtCore.QRect(210, 70, 151, 101))
        self.koloBUTTON.setStyleSheet("background:rgb(0, 153, 255)\n"
                                      "QPuschButton(color: black)\n"
                                      "\n"
                                      "")
        self.koloBUTTON.setObjectName("koloBUTTON")
        self.prostokatBUTTON = QtWidgets.QPushButton(Form)
        self.prostokatBUTTON.setGeometry(QtCore.QRect(400, 70, 151, 101))
        self.prostokatBUTTON.setStyleSheet("background:rgb(0, 153, 255)\n"
                                           "QPuschButton(color: black)\n"
                                           "\n"
                                           "")
        self.prostokatBUTTON.setObjectName("prostokatBUTTON")
        self.rownoleglobokBUTTON = QtWidgets.QPushButton(Form)
        self.rownoleglobokBUTTON.setGeometry(QtCore.QRect(400, 230, 151, 101))
        self.rownoleglobokBUTTON.setStyleSheet("background:rgb(0, 153, 255)\n"
                                               "QPuschButton(color: black)\n"
                                               "\n"
                                               "")
        self.rownoleglobokBUTTON.setObjectName("rownoleglobokBUTTON")
        self.trojkatBUTTON = QtWidgets.QPushButton(Form)
        self.trojkatBUTTON.setGeometry(QtCore.QRect(20, 230, 151, 101))
        self.trojkatBUTTON.setStyleSheet("background:rgb(0, 153, 255)\n"
                                         "QPuschButton(color: black)\n"
                                         "\n"
                                         "")
        self.trojkatBUTTON.setObjectName("trojkatBUTTON")
        self.rombBUTTON = QtWidgets.QPushButton(Form)
        self.rombBUTTON.setGeometry(QtCore.QRect(210, 230, 151, 101))
        self.rombBUTTON.setStyleSheet("background:rgb(0, 153, 255)\n"
                                      "QPuschButton(color: black)\n"
                                      "\n"
                                      "")
        self.rombBUTTON.setObjectName("rombBUTTON")
        self.exitBUTTON = QtWidgets.QPushButton(Form)
        self.exitBUTTON.setGeometry(QtCore.QRect(400, 470, 141, 31))
        self.exitBUTTON.setStyleSheet("background:rgb(0, 153, 255)\n"
                                      "QPuschButton(color: black)\n"
                                      "\n"
                                      "")
        self.exitBUTTON.setObjectName("exitBUTTON")
        self.trapezBUTTON = QtWidgets.QPushButton(Form)
        self.trapezBUTTON.setGeometry(QtCore.QRect(20, 400, 151, 101))
        self.trapezBUTTON.setStyleSheet("background:rgb(0, 153, 255)\n"
                                        "QPuschButton(color: black)\n"
                                        "\n"
                                        "")
        self.trapezBUTTON.setObjectName("trapezBUTTON")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 400, 151, 101))
        self.pushButton_9.setStyleSheet("background:rgb(0, 153, 255)\n"
                                        "QPuschButton(color: black)\n"
                                        "\n"
                                        "")
        self.pushButton_9.setObjectName("pushButton_9")
        self.helpButton = QtWidgets.QPushButton(Form)
        self.helpButton.setGeometry(QtCore.QRect(400, 400, 141, 31))
        self.helpButton.setStyleSheet("background:rgb(0, 153, 255)\n"
                                      "QPuschButton(color: black)\n"
                                      "\n"
                                      "")
        self.helpButton.setObjectName("helpButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KALKULATOR FIGUR PŁASKICH"))
        self.KwadratButton.setText(_translate("Form", "KWADRAT"))
        self.koloBUTTON.setText(_translate("Form", "KOŁO"))
        self.prostokatBUTTON.setText(_translate("Form", "PROSTOKĄT"))
        self.rownoleglobokBUTTON.setText(_translate("Form", "RÓWNOLEGŁOBOK"))
        self.trojkatBUTTON.setText(_translate("Form", "TRÓJKĄT"))
        self.rombBUTTON.setText(_translate("Form", "ROMB"))
        self.exitBUTTON.setText(_translate("Form", "EXIT"))
        self.trapezBUTTON.setText(_translate("Form", "TRAPEZ"))
        self.pushButton_9.setText(_translate("Form", "DELTOID"))
        self.helpButton.setText(_translate("Form", "HELP"))

        # implement click button
        self.KwadratButton.clicked.connect(self.openKwadrat)
        self.koloBUTTON.clicked.connect(self.openKolo)
        self.prostokatBUTTON.clicked.connect(self.openProstokat)
        self.rownoleglobokBUTTON.clicked.connect(self.openRownoleglobok)
        self.trojkatBUTTON.clicked.connect(self.openTrojkat)
        self.rombBUTTON.clicked.connect(self.openRomb)
        self.exitBUTTON.clicked.connect(self.Exit)
        self.trapezBUTTON.clicked.connect(self.openTrapez)
        self.pushButton_9.clicked.connect(self.openDeltoid)
        self.helpButton.clicked.connect(self.openHelp)

    def openKwadrat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kwadrat()
        self.ui.setupUi(self.window)
        self.window.show()

    def openKolo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kolo()
        self.ui.setupUi(self.window)
        self.window.show()

    def openProstokat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Prostokat()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRownoleglobok(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kwadrat()
        self.ui.setupUi(self.window)
        self.window.show()

    def openTrojkat(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kwadrat()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRomb(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kwadrat()
        self.ui.setupUi(self.window)
        self.window.show()



    def Exit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        choice = QMessageBox.question(self, 'Quit', 'Czy napewno chcesz wyjść?',
                                      (QMessageBox.Yes | QMessageBox.No))
        if choice == QMessageBox.Yes:
            exit(0)


    def openTrapez(self):
        self.ui = Ui_Kwadrat()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDeltoid(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kwadrat()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHelp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kwadrat()
        self.ui.setupUi(self.window)
        self.window.show()
