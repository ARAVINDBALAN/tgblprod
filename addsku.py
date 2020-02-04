# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmodsku.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(669, 441)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 491, 291))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 221, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.searchsku = QtGui.QPushButton(Dialog)
        self.searchsku.setGeometry(QtCore.QRect(250, 30, 93, 28))
        self.searchsku.setObjectName(_fromUtf8("searchsku"))
        self.addsku = QtGui.QPushButton(Dialog)
        self.addsku.setGeometry(QtCore.QRect(540, 80, 93, 28))
        self.addsku.setObjectName(_fromUtf8("addsku"))
        self.save = QtGui.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(540, 120, 93, 28))
        self.save.setObjectName(_fromUtf8("save"))
        self.exitbutton = QtGui.QPushButton(Dialog)
        self.exitbutton.setGeometry(QtCore.QRect(540, 160, 93, 28))
        self.exitbutton.setObjectName(_fromUtf8("exitbutton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.searchsku.setText(_translate("Dialog", "Search SKU", None))
        self.addsku.setText(_translate("Dialog", "Add SKU", None))
        self.save.setText(_translate("Dialog", "Save", None))
        self.exitbutton.setText(_translate("Dialog", "Exit", None))

