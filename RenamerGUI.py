import maya.cmds as mc
import sys
from PySide import QtCore, QtGui, QtUiTools

#Imports .ui file
class RenamerUI(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("C:\Users\michelle.hill\PycharmProjects\Learning\Renamer.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self)
        
        #Add button functions below


        file.close()


#MAYA FUNCTIONS BELOW...
    def textEdit(self):
        self.myLayout = QVBoxLayout(RenamerUI)
        obj = mc.ls(sl=True)
        items = obj[0:]

#Select objects..."x" selections will generate "x" text fields in window
#sel = mc.ls(sl=True)

#Text field
#textBox = QWidget.QLineEdit()
#items = obj[0:]

#for x in items:


if __name__ == "__main__":
    # Set up application with any command line args
    #app = QtGui.QApplication(sys.argv)
    
    ui = RenamerUI()

    ui.show()

    # Lastly, when we are done... EXIT
    #sys.exit(app.exec_())
