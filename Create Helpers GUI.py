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
        
        #Connects buttons
        self.myWidget.locBttn.clicked.connect(createLoc)
        #self.myWidget.mrkrBttn.clicked.connect(createSensor)
        file.close()
    
    #Defined function for creating locator(s)        
    def createLoc():
        mc.spaceLocator()   
        createLoc()
    
       
    
'''    
    def createMrkr():
        mrkr = mc.polySphere(n="marker", sx=20, sy=20, r=.20)
        mc.color(mrkr, rgb=(0.663, 0.182, 0.482))
        createMrkr()    
'''                   
        #parents to Maya Window..its not working...
        #parent = getMayaWindow()
        
        
if __name__ == "__main__":
   
    ui = Ui_MainWindow()
    
    ui.show()

