import sys
from MainWindow import Ui_Dialog
from SortingWindow import Ui_SortingTechniques
from PyQt5 import QtWidgets

class Sorting():
    def __init__(self):
        self.ui_Welcome = Ui_Dialog()
        self.ui_Sorting = Ui_SortingTechniques()
        self.app = QtWidgets.QApplication(sys.argv)
        
    def calSort(self):
        SortingTechniques = QtWidgets.QWidget()
        self.ui_Sorting.setupUi(SortingTechniques)
        SortingTechniques.show()
        sys.exit(self.app.exec_())
    
    def calMain(self):
        Dialog = QtWidgets.QDialog()
        self.ui_Welcome.setupUi(Dialog)
        Dialog.show()
        if Dialog.exec_():
            self.calSort()
            
if __name__=="__main__":
    sort = Sorting()
    sort.calMain()
            