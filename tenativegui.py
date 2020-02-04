from nooftruck import ddd,killdill
import sys
from PyQt4 import QtCore, QtGui
from tenativeui import Ui_Dialog
from database import select_from_tenative,select_from_missing_sku,delete_missing_sku
class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.missingsku.setSelectionMode(QtGui.QListWidget.MultiSelection)
        self.ui.load_ten.clicked.connect(self.load_data)
        self.ui.skunames.clicked.connect(self.load_sku_missing)
        self.ui.delsku.clicked.connect(self.del_from_missing)
        #self.ui.tenativetable.setHorizontalHeaderLabels(cols)
        #self.ui.exitbutton.clicked.connect(self.close_screen)
    @QtCore.pyqtSignature("")
    def load_data(self):
        res = select_from_tenative()
        self.ui.tenativetable.setRowCount(20)
        cols = []
        rows = []
        for i in res:
            cols.append(i[0])
            print(i[1])
            temp = str(i[1])
            temp=temp.replace("]","")
            temp=temp.replace("'","")
            temp = temp.replace("[","")
            temp = temp.split(",")
            rows.append(temp)
        print(cols)
        ddd(killdill)
        print(rows)        
        self.ui.tenativetable.setColumnCount(len(cols))
        self.ui.tenativetable.setHorizontalHeaderLabels(cols)
        for i in range(len(cols)):
            for j in range(len(rows[i])):
                self.ui.tenativetable.setItem(j,i,QtGui.QTableWidgetItem(str(rows[i][j])))

    @QtCore.pyqtSignature("")
    def load_sku_missing(self):
        res = select_from_missing_sku()
        for i in res:
            self.ui.missingsku.addItem(str(i[0]))

    @QtCore.pyqtSignature("")
    def del_from_missing(self):
        selected = self.ui.missingsku.selectedItems() 
        to_db = []
        for i in selected:
            to_db.append(i.text())
        print(to_db)
        delete_missing_sku(to_db)
        from_db = select_from_missing_sku()
        self.ui.missingsku.clear()
        for i in from_db:
            self.ui.missingsku.addItem(str(i[0]))


if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    
    myapp.show()
    sys.exit(app.exec_())	

