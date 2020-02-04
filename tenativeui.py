# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mach.ui'
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
        Dialog.resize(1132, 649)
        self.load_ten = QtGui.QPushButton(Dialog)
        self.load_ten.setGeometry(QtCore.QRect(300, 570, 151, 28))
        self.load_ten.setObjectName(_fromUtf8("load_ten"))
        self.schedule = QtGui.QPushButton(Dialog)
        self.schedule.setGeometry(QtCore.QRect(880, 590, 93, 28))
        self.schedule.setObjectName(_fromUtf8("schedule"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 20, 161, 31))
        self.label.setMaximumSize(QtCore.QSize(161, 16777215))
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.tenativetable = QtGui.QTableWidget(Dialog)
        self.tenativetable.setGeometry(QtCore.QRect(60, 70, 661, 461))
        self.tenativetable.setRowCount(10)
        self.tenativetable.setColumnCount(10)
        self.tenativetable.setObjectName(_fromUtf8("tenativetable"))
        self.missingsku = QtGui.QListWidget(Dialog)
        self.missingsku.setGeometry(QtCore.QRect(790, 70, 256, 431))
        self.missingsku.setObjectName(_fromUtf8("missingsku"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(880, 40, 111, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.skunames = QtGui.QPushButton(Dialog)
        self.skunames.setGeometry(QtCore.QRect(810, 530, 93, 28))
        self.skunames.setObjectName(_fromUtf8("skunames"))
        self.delsku = QtGui.QPushButton(Dialog)
        self.delsku.setGeometry(QtCore.QRect(930, 530, 101, 28))
        self.delsku.setObjectName(_fromUtf8("delsku"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Tenative schedule", None))
        self.load_ten.setText(_translate("Dialog", "Load Tenative", None))
        self.schedule.setText(_translate("Dialog", "Schedule", None))
        self.label.setText(_translate("Dialog", "Tenative Truck Schedule", None))
        self.label_2.setText(_translate("Dialog", "Missing SKUs", None))
        self.skunames.setText(_translate("Dialog", "Show SKUs", None))
        self.delsku.setText(_translate("Dialog", "Remove SKU", None))

