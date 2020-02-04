
import sys
from PyQt4 import QtCore, QtGui
from alpha import Ui_Scheduler
from database import  insert_into_tenative,select_date_from_table,delete_dates_from_table,insert_into_work,insert_into_skudim,select_from_skudimpath,delete_from_tenative,insert_into_missing_sku
import skuaddgui
from nooftruck import tenative,volume_or_weight_map,schedule_two_week_truck,depo_day_map,depo_list,depo_truck,dummy,map_list,schedule_list,sort_by_date
import tenativegui
from datetime import date
from get_sku_format_with_depo import get_format_from_dim_km,get_sku_mach_config
#global variables 
li=[]
from sch30 import scheduler

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Scheduler()
        self.ui.setupUi(self)
        self.ui.browse_check.hide()
        self.ui.browse_check.setChecked(False)
        self.ui.Browse.clicked.connect(self.selectFile)
        self.initializedates()
        self.ui.proceedtonexttext.hide()
        self.ui.next.hide()
        self.ui.calendarWidget.clicked.connect(self.select_working_days)
        self.ui.confirm_date.clicked.connect(self.confirm_dates)
        self.skuaddguipy = skuaddgui.MyDialog()
        self.ui.modify_sku.clicked.connect(self.goto_skuaddgui)
        self.ui.datelistview.setSelectionMode(QtGui.QListWidget.MultiSelection)
        self.ui.datedeletebutton.clicked.connect(self.delete_dates)
        self.tenativegiu = tenativegui.MyDialog()
        self.ui.next.clicked.connect(self.goto_scheduler)
        self.ui.inputskudimension.clicked.connect(self.inputskuhere)
        self.ui.get_sku_format.clicked.connect(self.generate_op_from_km)
        self.ui.date.setText(str(date.today()))
        self.ui.day.setText(str(date.today().strftime("%A")))
        #self.ui.show_calc_ten.clicked.connect(self.show_calc_ten)
        self.ui.modify_machine.clicked.connect(self.modify_machines)
        self.ui.mach_browse.clicked.connect(self.get_mach_hopper_path)
    
    @QtCore.pyqtSignature("")
    def get_mach_hopper_path(self):
        path = QtGui.QFileDialog.getOpenFileName()
        self.ui.mach_hop.setText(str(path))

    @QtCore.pyqtSignature("")
    def goto_scheduler(self):
        indent = 4
        l1 = self.ui.l1_indent.isChecked()
        l2 = self.ui.l2_indent.isChecked()
        if(l1==True):
            indent = 1
        elif(l2==True):
            indent = 2
        mach_hopper_path = self.ui.mach_browse.text()
        datesfromtable = select_date_from_table("working_days")
        datelist = []
        for i in datesfromtable:
            datelist.append(i[0])
        scheduler("output_from_km_dimension.xlsx",datelist,mach_hopper_path,indent)
    
    @QtCore.pyqtSignature("")
    def goto_skuaddgui(self):
        self.skuaddguipy.show()
        
    @QtCore.pyqtSignature("")
    def inputskuhere(self):
        path = QtGui.QFileDialog.getOpenFileName()
        insert_into_skudim(str(path))

    @QtCore.pyqtSignature("")
    def show_calc_ten(self):
        self.tenativegiu.show()

    @QtCore.pyqtSignature("")
    def modify_machines(self):
        path = QtGui.QFileDialog.getOpenFileName()
        get_sku_mach_config(path)


    @QtCore.pyqtSignature("")
    def show_tenative(self):
        delete_from_tenative()
        datesfromtable = select_date_from_table("working_days")
        scheduledates = []
        for i in datesfromtable:
            scheduledates.append(str(i[0]))
        opfromten = tenative(scheduledates,"output_from_km_dimension.xlsx")
        opfromvolorweight = volume_or_weight_map(opfromten)
        count = 0
        for n in opfromvolorweight:
            count += n[1]
        opfromten = schedule_two_week_truck(scheduledates,opfromvolorweight,depo_truck,depo_list)
        datedict = sort_by_date(opfromten,scheduledates,count)
        print(datedict)
        for i in datedict:
            print("xfgfgjfjb")
            temp_to_database = [str(i),str(datedict[i])]
            insert_into_tenative(temp_to_database)

        self.tenativegiu.show()



    @QtCore.pyqtSignature("")
    def selectFile(self):
        self.ui.path.setText(QtGui.QFileDialog.getOpenFileName())
        self.ui.browse_check.show()
        self.ui.browse_check.setChecked(True)


    @QtCore.pyqtSignature("")
    def select_working_days(self):
        select_date = self.ui.calendarWidget.selectedDate()
        if(select_date in li):
            li.remove(select_date.toPyDate())
        else:
            li.append(select_date.toPyDate())
        


    @QtCore.pyqtSignature("")
    def initializedates(self):
        res = select_date_from_table("working_days")
        for i in res:
            self.ui.datelistview.addItem(str(i[0]))
        

    @QtCore.pyqtSignature("")
    def confirm_dates(self):
        global li
        self.ui.datelistview.clear()
        string_dates = []
        for i in range(len(li)):
            string_dates.append(str(li[i]))
        res = select_date_from_table("working_days")
        table_dates = []
        for i in res:
            table_dates.append(i[0])
        print(table_dates)
        for i in table_dates:
            if i in string_dates:
                string_dates.remove(i)  
                delete_dates_from_table(i)
        insert_into_work(string_dates)
        res = select_date_from_table("working_days")

        for i in res:
            self.ui.datelistview.addItem(str(i[0]))
        li=[]


    @QtCore.pyqtSignature("")
    def generate_op_from_km(self):
        datesfromtable = select_date_from_table("working_days")
        scheduledates = []
        for i in datesfromtable:
            scheduledates.append(str(i[0]))
        dm = select_from_skudimpath()
        for i in dm:
            pathtodm = i[1]
        print(pathtodm)
        missing = get_format_from_dim_km(str(self.ui.path.text()),str(pathtodm))
        insert_into_missing_sku(missing)        
        self.ui.next.show()
        self.ui.proceedtonexttext.show()



    @QtCore.pyqtSignature("")
    def delete_dates(self):
        dates_to_delete = self.ui.datelistview.selectedItems()
        for i in dates_to_delete:
            delete_dates_from_table(i.text())
        self.ui.datelistview.clear()
        res = select_date_from_table("working_days")
        for i in res:
            self.ui.datelistview.addItem(str(i[0]))


if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())	
