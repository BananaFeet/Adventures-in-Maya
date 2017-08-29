#Create Helpers GUI
import sys
import maya.cmds as mc
from PySide import QtCore, QtGui, QtUiTools
    
class Ui_MainWindow(QtGui.QWidget):
    def __init__(self):
        #Loads the directed '.ui' file
        QtGui.QWidget.__init__(self)
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("C:\Users\michelle.hill\PycharmProjects\Learning\Create_Helpers.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self)
        file.close()      
        
    #Make the button work with using a "Decorator". A decorator is a function 
    #that takes on another function and extends the behavior of the latter 
    #function without modifying it.
    @QtCore.Slot(name='on_OKbttn_pressed')#The buttons currently don't work.
    def buttonclicked(self):
        print "HELLO"
        self.myWidget.textEdit.setText("stuff")
if __name__ == "__main__":
   
    ui = Ui_MainWindow()
    
    ui.show()
