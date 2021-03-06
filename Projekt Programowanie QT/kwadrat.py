# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kwadrat.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QDoubleValidator, QRegExpValidator, QIcon
from PyQt5.QtWidgets import QMessageBox


class Ui_Kwadrat(object):
    def setupUi(self, Kwadrat):
        Kwadrat.setObjectName("Kwadrat")
        Kwadrat.resize(300, 300)
        Kwadrat.setMinimumSize(QtCore.QSize(300, 300))
        Kwadrat.setMaximumSize(QtCore.QSize(300, 300))
        Kwadrat.setWindowIcon(QIcon('logo.png'))
        Kwadrat.setStyleSheet("background-image: url(tlopodstrony.png);")

        self.label = QtWidgets.QLabel(Kwadrat)
        self.label.setGeometry(QtCore.QRect(60, 30, 190, 31))
        self.label.setStyleSheet("background:rgb(255, 255, 255)")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
       ## self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(0)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Kwadrat)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.lineEdit.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.lineEdit.setObjectName("lineEdit")
        # self.lineEdit.setValidator(QDoubleValidator(1.0, 100.0, 6))
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("[0.1-9.9]*")))
        self.lineEdit.setText('0')

        self.pushButton = QtWidgets.QPushButton(Kwadrat)

        self.pushButton.setGeometry(QtCore.QRect(100, 120, 93, 28))
        self.pushButton.setStyleSheet("background:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(Kwadrat)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 101, 31))
        self.label_2.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
       ## self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(2)
        self.label_2.setMidLineWidth(0)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Kwadrat)
        self.label_3.setGeometry(QtCore.QRect(170, 170, 120, 31))
        self.label_3.setStyleSheet("background:rgb(255, 255, 255)")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
       ## self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(2)
        self.label_3.setMidLineWidth(0)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")

        self.lcdNumber = QtWidgets.QLCDNumber(Kwadrat)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 220, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(Kwadrat)
        self.lcdNumber_2.setGeometry(QtCore.QRect(190, 220, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.retranslateUi(Kwadrat)
        QtCore.QMetaObject.connectSlotsByName(Kwadrat)

    def retranslateUi(self, Kwadrat):
        _translate = QtCore.QCoreApplication.translate
        Kwadrat.setWindowTitle(_translate("Kwadrat", "KWADRAT"))
        self.label.setText(_translate("Kwadrat", "Wpisz długość boku kwadratu"))
        self.pushButton.setText(_translate("Kwadrat", "Oblicz"))
        self.label_2.setText(_translate("Kwadrat", "Pole kwadratu"))
        self.label_3.setText(_translate("Kwadrat", "Obwód kwadratu"))


        self.pushButton.clicked.connect(self.wykonaj)



    def wykonaj(self):

        zmienna1 = self.lineEdit.text()
        polekwadratu = float(zmienna1) * float(zmienna1)
        obwodkwadratu = float(zmienna1) * 4



        if (float(zmienna1)) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wpisałes błedną(e) wartość")
            msg.setInformativeText('Długość nie moze wynosic 0')
            msg.setWindowTitle("Błąd")
            msg.exec_()
        else:
            self.lcdNumber.display(float(polekwadratu))
            self.lcdNumber_2.display(float(obwodkwadratu))
