#Create Helpers GUI
import sys
import maya.cmds as mc
import maya.OpenMayaUI as omui #access maya api
import shiboken
from PySide import QtCore, QtGui, QtUiTools

#Parent to Maya window. This is reusable for future GUIs.
def getMayaWindow():
    #Set pointer to get main window in maya
    pointer = omui.MQtUtil.mainWindow()
    #Wrap instance creates a wrapper for C++ object at given memory address. 'wrapInstance' takes two arguments:
    # an int and type. 
    return shiboken.wrapInstance(long(pointer), QtGui.QWidget)
    
class Ui_MainWindow(QtGui.QWidget):
    def __init__(self):
        #Loads the directed '.ui' file
        QtGui.QWidget.__init__(self)
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("C:\Users\michelle.hill\PycharmProjects\Learning\Create_Helpers.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self)
        file.close()

#Button functions
    def createButtons(self):
        
        #Create locator button
        locBttn = QPushButton()
        
        #parents to Maya Window..its not working...
        #parent = getMayaWindow()
        
'''  Omit this temporarily    
    #Make the button work with using a "Decorator". A decorator is a function 
    #that takes on another function and extends the behavior of the latter 
    #function without modifying it.
    @QtCore.Slot(name='on_OKbttn_pressed')#The buttons currently don't work.
    def buttonclicked(self):
        print "HELLO"
        self.myWidget.textEdit.setText("stuff")
'''
        
if __name__ == "__main__":
   
    ui = Ui_MainWindow()
    
    ui.show()
