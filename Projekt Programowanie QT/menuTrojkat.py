# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuTrojkat.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from rownoboczny import Ui_Rownoboczny
from roznoboczny import Ui_Roznoboczny


class Ui_MenuTrojkat(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 231)
        Form.setMinimumSize(QtCore.QSize(380, 231))
        Form.setMaximumSize(QtCore.QSize(380, 231))
        Form.setMinimumSize(QtCore.QSize(20, 20))
        Form.setStyleSheet("background:rgb(255, 225, 255)")
        self.roznobocznyButton = QtWidgets.QPushButton(Form)
        self.roznobocznyButton.setEnabled(True)
        self.roznobocznyButton.setGeometry(QtCore.QRect(20, 70, 151, 101))
        self.roznobocznyButton.setMouseTracking(False)
        self.roznobocznyButton.setTabletTracking(False)
        self.roznobocznyButton.setAcceptDrops(False)
        self.roznobocznyButton.setAutoFillBackground(False)
        self.roznobocznyButton.setStyleSheet("background:rgb(0, 153, 255)\n"
"QPuschButton(color: black)\n"
"\n"
"")
        self.roznobocznyButton.setCheckable(False)
        self.roznobocznyButton.setAutoRepeat(False)
        self.roznobocznyButton.setAutoDefault(False)
        self.roznobocznyButton.setDefault(False)
        self.roznobocznyButton.setFlat(False)
        self.roznobocznyButton.setObjectName("roznobocznyButton")
        self.rownobocznyButton = QtWidgets.QPushButton(Form)
        self.rownobocznyButton.setGeometry(QtCore.QRect(200, 70, 161, 101))
        self.rownobocznyButton.setStyleSheet("background:rgb(0, 153, 255)\n"
"QPuschButton(color: black)\n"
"\n"
"")
        self.rownobocznyButton.setObjectName("rownobocznyButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MENU TRÓJKĄT"))
        self.roznobocznyButton.setText(_translate("Form", "TRÓJKĄT RÓŻNOBOCZNY"))
        self.rownobocznyButton.setText(_translate("Form", "TRÓJKĄT RÓWNOBOCZNY"))

        self.roznobocznyButton.clicked.connect(self.openRoznoboczny)
        self.rownobocznyButton.clicked.connect(self.openRownoboczny)




    def openRownoboczny(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Rownoboczny()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRoznoboczny(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Roznoboczny()
        self.ui.setupUi(self.window)
        self.window.show()

