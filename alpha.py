# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scheduler_main.ui'
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

class Ui_Scheduler(object):
    def setupUi(self, Scheduler):
        Scheduler.setObjectName(_fromUtf8("Scheduler"))
        Scheduler.resize(1345, 741)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Scheduler.setWindowIcon(icon)
        Scheduler.setStyleSheet(_fromUtf8(""))
        self.modify_sku = QtGui.QPushButton(Scheduler)
        self.modify_sku.setGeometry(QtCore.QRect(940, 400, 261, 41))
        self.modify_sku.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.modify_sku.setObjectName(_fromUtf8("modify_sku"))
        self.line = QtGui.QFrame(Scheduler)
        self.line.setGeometry(QtCore.QRect(890, 70, 20, 711))
        self.line.setStyleSheet(_fromUtf8("color: rgb(231, 226, 220);"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.path = QtGui.QLineEdit(Scheduler)
        self.path.setGeometry(QtCore.QRect(940, 110, 261, 29))
        self.path.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.path.setObjectName(_fromUtf8("path"))
        self.Browse = QtGui.QPushButton(Scheduler)
        self.Browse.setGeometry(QtCore.QRect(1210, 110, 100, 31))
        self.Browse.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.Browse.setObjectName(_fromUtf8("Browse"))
        self.modify_machine = QtGui.QPushButton(Scheduler)
        self.modify_machine.setGeometry(QtCore.QRect(940, 470, 261, 41))
        self.modify_machine.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.modify_machine.setObjectName(_fromUtf8("modify_machine"))
        self.next = QtGui.QPushButton(Scheduler)
        self.next.setGeometry(QtCore.QRect(940, 670, 261, 41))
        self.next.setStyleSheet(_fromUtf8("background-color: violet;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.next.setObjectName(_fromUtf8("next"))
        self.calendarWidget = QtGui.QCalendarWidget(Scheduler)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 100, 521, 341))
        self.calendarWidget.setStyleSheet(_fromUtf8("color: rgb(85, 85, 255);\n"
"background-color: rgb(0, 0, 10);"))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.date = QtGui.QLabel(Scheduler)
        self.date.setGeometry(QtCore.QRect(1210, 10, 141, 20))
        self.date.setStyleSheet(_fromUtf8(""))
        self.date.setObjectName(_fromUtf8("date"))
        self.day = QtGui.QLabel(Scheduler)
        self.day.setGeometry(QtCore.QRect(1210, 40, 141, 20))
        self.day.setObjectName(_fromUtf8("day"))
        self.browse_check = QtGui.QCheckBox(Scheduler)
        self.browse_check.setGeometry(QtCore.QRect(910, 110, 21, 31))
        self.browse_check.setText(_fromUtf8(""))
        self.browse_check.setObjectName(_fromUtf8("browse_check"))
        self.browse_check_2 = QtGui.QCheckBox(Scheduler)
        self.browse_check_2.setGeometry(QtCore.QRect(30, 470, 96, 20))
        self.browse_check_2.setText(_fromUtf8(""))
        self.browse_check_2.setObjectName(_fromUtf8("browse_check_2"))
        self.confirm_date = QtGui.QPushButton(Scheduler)
        self.confirm_date.setGeometry(QtCore.QRect(410, 580, 261, 41))
        self.confirm_date.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.confirm_date.setObjectName(_fromUtf8("confirm_date"))
        self.label_2 = QtGui.QLabel(Scheduler)
        self.label_2.setGeometry(QtCore.QRect(90, 540, 201, 20))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.datelistview = QtGui.QListWidget(Scheduler)
        self.datelistview.setGeometry(QtCore.QRect(70, 490, 231, 241))
        self.datelistview.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.datelistview.setObjectName(_fromUtf8("datelistview"))
        self.datedeletebutton = QtGui.QPushButton(Scheduler)
        self.datedeletebutton.setGeometry(QtCore.QRect(410, 650, 261, 41))
        self.datedeletebutton.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.datedeletebutton.setObjectName(_fromUtf8("datedeletebutton"))
        self.label_4 = QtGui.QLabel(Scheduler)
        self.label_4.setGeometry(QtCore.QRect(1050, 80, 281, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.inputskudimension = QtGui.QPushButton(Scheduler)
        self.inputskudimension.setGeometry(QtCore.QRect(940, 180, 261, 41))
        self.inputskudimension.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.inputskudimension.setObjectName(_fromUtf8("inputskudimension"))
        self.get_sku_format = QtGui.QPushButton(Scheduler)
        self.get_sku_format.setGeometry(QtCore.QRect(940, 240, 261, 41))
        self.get_sku_format.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.get_sku_format.setObjectName(_fromUtf8("get_sku_format"))
        self.proceedtonexttext = QtGui.QLabel(Scheduler)
        self.proceedtonexttext.setGeometry(QtCore.QRect(950, 300, 311, 41))
        self.proceedtonexttext.setObjectName(_fromUtf8("proceedtonexttext"))
        self.label_5 = QtGui.QLabel(Scheduler)
        self.label_5.setGeometry(QtCore.QRect(150, 50, 331, 41))
        self.label_5.setMinimumSize(QtCore.QSize(121, 0))
        self.label_5.setStyleSheet(_fromUtf8("font: 75 12pt \"Roboto\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.495 rgba(255, 255, 255, 255), stop:0.505 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label = QtGui.QLabel(Scheduler)
        self.label.setGeometry(QtCore.QRect(990, 360, 161, 20))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"MS Sans Serif\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.depo_add = QtGui.QPushButton(Scheduler)
        self.depo_add.setGeometry(QtCore.QRect(940, 540, 261, 41))
        self.depo_add.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.depo_add.setObjectName(_fromUtf8("depo_add"))
        self.depo_add_2 = QtGui.QPushButton(Scheduler)
        self.depo_add_2.setGeometry(QtCore.QRect(940, 600, 261, 41))
        self.depo_add_2.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.depo_add_2.setObjectName(_fromUtf8("depo_add_2"))
        self.l1_indent = QtGui.QRadioButton(Scheduler)
        self.l1_indent.setGeometry(QtCore.QRect(1080, 150, 105, 21))
        self.l1_indent.setObjectName(_fromUtf8("l1_indent"))
        self.l2_indent = QtGui.QRadioButton(Scheduler)
        self.l2_indent.setGeometry(QtCore.QRect(950, 150, 105, 21))
        self.l2_indent.setObjectName(_fromUtf8("l2_indent"))
        self.mach_hop = QtGui.QLineEdit(Scheduler)
        self.mach_hop.setGeometry(QtCore.QRect(570, 110, 281, 32))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.mach_hop.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mach_hop.setFont(font)
        self.mach_hop.setObjectName(_fromUtf8("mach_hop"))
        self.label_3 = QtGui.QLabel(Scheduler)
        self.label_3.setGeometry(QtCore.QRect(580, 80, 231, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.mach_browse = QtGui.QPushButton(Scheduler)
        self.mach_browse.setGeometry(QtCore.QRect(570, 160, 100, 31))
        self.mach_browse.setStyleSheet(_fromUtf8("background-color: orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: white;\n"
"padding: 4px;"))
        self.mach_browse.setObjectName(_fromUtf8("mach_browse"))

        self.retranslateUi(Scheduler)
        QtCore.QMetaObject.connectSlotsByName(Scheduler)

    def retranslateUi(self, Scheduler):
        Scheduler.setWindowTitle(_translate("Scheduler", "Scheduler Application for PULP", None))
        self.modify_sku.setText(_translate("Scheduler", "SKU", None))
        self.Browse.setText(_translate("Scheduler", "Browse", None))
        self.modify_machine.setText(_translate("Scheduler", "MACHINE CONFIG", None))
        self.next.setText(_translate("Scheduler", "Schedule", None))
        self.date.setText(_translate("Scheduler", "TextLabel", None))
        self.day.setText(_translate("Scheduler", "TextLabel", None))
        self.confirm_date.setText(_translate("Scheduler", "Confirm date", None))
        self.label_2.setText(_translate("Scheduler", "Selected days for scheduling", None))
        self.datedeletebutton.setText(_translate("Scheduler", "Delete selected days", None))
        self.label_4.setText(_translate("Scheduler", "Input KM Tracker file here ", None))
        self.inputskudimension.setText(_translate("Scheduler", "Input SKU dimension", None))
        self.get_sku_format.setText(_translate("Scheduler", "Generate formatted input from KM", None))
        self.proceedtonexttext.setText(_translate("Scheduler", "Output generted from KM Tracker and \n"
"Sku Dimension , proceed to \"Next\" ", None))
        self.label_5.setText(_translate("Scheduler", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">SELECT WORKING DAYS</span></p></body></html>", None))
        self.label.setText(_translate("Scheduler", "ADD/MODIFY", None))
        self.depo_add.setText(_translate("Scheduler", "DEPO", None))
        self.depo_add_2.setText(_translate("Scheduler", "BLEND", None))
        self.l1_indent.setText(_translate("Scheduler", "L1 INDENT", None))
        self.l2_indent.setText(_translate("Scheduler", "L2 INDENT", None))
        self.label_3.setText(_translate("Scheduler", "Input Machine Hopper Path here ", None))
        self.mach_browse.setText(_translate("Scheduler", "Browse", None))

