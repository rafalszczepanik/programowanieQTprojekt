# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Romb.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Romb(object):


    def setupUi(self, Romb):
        Romb.setObjectName("Romb")
        Romb.resize(300, 300)
        Romb.setMinimumSize(QtCore.QSize(300, 300))
        Romb.setMaximumSize(QtCore.QSize(300, 300))
        Romb.setStyleSheet("background:rgb(11, 198, 205)")
        self.label = QtWidgets.QLabel(Romb)
        self.label.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.label.setStyleSheet("labelcolor:rgb(204, 204, 204)")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")

        self.obliczButton = QtWidgets.QPushButton(Romb)
        self.obliczButton.setGeometry(QtCore.QRect(100, 120, 93, 28))
        self.obliczButton.setStyleSheet("background:rgb(255, 255, 255)")
        self.obliczButton.setObjectName("obliczButton")

        self.label_2 = QtWidgets.QLabel(Romb)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 101, 31))
        self.label_2.setStyleSheet("labelcolor:rgb(204, 204, 204)")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(1)
        self.label_2.setMidLineWidth(0)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Romb)
        self.label_3.setGeometry(QtCore.QRect(170, 170, 121, 31))
        self.label_3.setStyleSheet("labelcolor:rgb(204, 204, 204)")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(0)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")

        self.lcdPoleRombu = QtWidgets.QLCDNumber(Romb)
        self.lcdPoleRombu.setGeometry(QtCore.QRect(40, 220, 64, 23))
        self.lcdPoleRombu.setObjectName("lcdPoleRombu")
        self.lcdObwodRombu = QtWidgets.QLCDNumber(Romb)
        self.lcdObwodRombu.setGeometry(QtCore.QRect(190, 220, 64, 23))
        self.lcdObwodRombu.setObjectName("lcdObwodRombu")

        self.lineEdit_wysokosc = QtWidgets.QLineEdit(Romb)
        self.lineEdit_wysokosc.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.lineEdit_wysokosc.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit_wysokosc.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEdit_wysokosc.setValidator(QtGui.QIntValidator(1, 999))
        self.lineEdit_wysokosc.setObjectName("lineEdit_wysokosc")


        self.label_4 = QtWidgets.QLabel(Romb)
        self.label_4.setGeometry(QtCore.QRect(150, 30, 141, 31))
        self.label_4.setStyleSheet("labelcolor:rgb(204, 204, 204)")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(1)
        self.label_4.setMidLineWidth(0)
        self.label_4.setWordWrap(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")

        self.lineEdit_bok_a = QtWidgets.QLineEdit(Romb)
        self.lineEdit_bok_a.setGeometry(QtCore.QRect(30, 70, 113, 22))
        self.lineEdit_bok_a.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_bok_a.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit_bok_a.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_bok_a.setText("")
        self.lineEdit_bok_a.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEdit_bok_a.setObjectName("lineEdit_bok_a")
        self.lineEdit_bok_a.setValidator(QtGui.QIntValidator(0, 999))

        self.retranslateUi(Romb)
        QtCore.QMetaObject.connectSlotsByName(Romb)

    def retranslateUi(self, Romb):
        _translate = QtCore.QCoreApplication.translate
        Romb.setWindowTitle(_translate("Romb", "ROMB"))
        self.label.setText(_translate("Romb", "Wpisz długość boku a"))
        self.obliczButton.setText(_translate("Romb", "Oblicz"))
        self.label_2.setText(_translate("Romb", "Pole rombu"))
        self.label_3.setText(_translate("Romb", "Obwód rombu"))
        self.label_4.setText(_translate("Romb", "Wpisz wysokość"))

        self.obliczButton.clicked.connect(self.wykonaj)

    def wykonaj(self):

       zmienna1 = self.lineEdit_bok_a.text()
       zmienna2 = self.lineEdit_wysokosc.text()

       polerombu = int(zmienna1) * int(zmienna2)
       obwodrombu = int(zmienna1) * 4
       self.lcdPoleRombu.display(polerombu)
       self.lcdObwodRombu.display(obwodrombu)
