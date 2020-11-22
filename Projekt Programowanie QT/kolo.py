# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kolo.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kolo(object):
    def setupUi(self, Kolo):
        Kolo.setObjectName("Kolo")
        Kolo.resize(300, 300)
        Kolo.setMinimumSize(QtCore.QSize(300, 300))
        Kolo.setMaximumSize(QtCore.QSize(300, 300))
        Kolo.setStyleSheet("background:rgb(11, 198, 205)")
        self.label = QtWidgets.QLabel(Kolo)
        self.label.setGeometry(QtCore.QRect(60, 30, 181, 31))
        self.label.setStyleSheet("labelcolor:rgb(204, 204, 204)")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(4)
        self.label.setMidLineWidth(0)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Kolo)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.lineEdit.setStyleSheet("background:rgb(255, 255, 255)")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Kolo)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 93, 28))
        self.pushButton.setStyleSheet("background:rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Kolo)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 101, 31))
        self.label_2.setStyleSheet("labelcolor:rgb(204, 204, 204)")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(4)
        self.label_2.setMidLineWidth(0)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Kolo)
        self.label_3.setGeometry(QtCore.QRect(170, 170, 111, 31))
        self.label_3.setStyleSheet("labelcolor:rgb(204, 204, 204)")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(4)
        self.label_3.setMidLineWidth(0)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(Kolo)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 220, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Kolo)
        self.lcdNumber_2.setGeometry(QtCore.QRect(190, 220, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.retranslateUi(Kolo)
        QtCore.QMetaObject.connectSlotsByName(Kolo)

    def retranslateUi(self, Kwadrat):
        _translate = QtCore.QCoreApplication.translate
        Kwadrat.setWindowTitle(_translate("Kolo", "KOŁO"))
        self.label.setText(_translate("Kolo", "Wpisz długość promienia"))
        self.pushButton.setText(_translate("Kolo", "Oblicz"))
        self.label_2.setText(_translate("Kolo", "Pole koła"))
        self.label_3.setText(_translate("Kolo", "Obwód koła"))

        self.pushButton.clicked.connect(self.wykonaj)

    def wykonaj(self):
            zmienna1 = self.lineEdit.text()
            pom = 3.14
            polekola = (int(zmienna1) * int(zmienna1))* pom
            obwodkola = int(zmienna1) * 2
            self.lcdNumber.display(polekola)
            self.lcdNumber_2.display(obwodkola)
