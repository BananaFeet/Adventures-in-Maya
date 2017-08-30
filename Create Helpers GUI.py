# Create Helpers GUI
import sys
import maya.cmds as mc
import maya.OpenMayaUI as omui  # access maya api
import shiboken
from PySide import QtCore, QtGui, QtUiTools

'''OMIT TERMPORARILY
#Parent to Maya window. This is reusable for future GUIs.
def getMayaWindow():
    #Set pointer to get main window in maya
    pointer = omui.MQtUtil.mainWindow()
    #parent = getMayaWindow()
    #Wrap instance creates a wrapper for C++ object at given memory address. 'wrapInstance' takes two arguments:
    # an int and type.
    return shiboken.wrapInstance(long(pointer), QtGui.QWidget)
'''


class mainUI(QtGui.QWidget):
    # "__init__" is a constructor that is automatically called when a new instance of a class is created
    def __init__(self):
        # Loads the directed '.ui' file
        QtGui.QWidget.__init__(self)
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("C:\Users\michelle.hill\PycharmProjects\Learning\Create_Helpers.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self)

        # Connects buttons
        self.myWidget.locBttn.clicked.connect(self.createLoc)
        self.myWidget.mrkrBttn.clicked.connect(self.createSensor)
        self.myWidget.closeBttn.clicked.connect(self.exitWin)
        file.close()

    # Defined function for creating locator(s)
    def createLoc(self):
        print "I'm helping!"
        mc.spaceLocator()

        # Defined function for creating marker(s)

    def createSensor(self):
        print "I'm helping!"
        mc.polySphere(n="marker", sx=20, sy=20, r=.20)
        # mc.color(sensor, rgb=(0.663, 0.182, 0.482))

    # Defined function for closing UI
    def exitWin(self):
        print "Create Helpers window has closed"
        self.close()


if __name__ == "__main__":
    ui = mainUI()

    ui.show()
