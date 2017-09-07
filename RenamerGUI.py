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
        #When Gui object has an event, connect it to the designated function that is 
        #listed in the "()".  
        self.myWidget.listSel.itemClicked.connect(self.listedItem)
        self.myWidget.closeBttn.clicked.connect(self.exitWin)
        self.myWidget.editName.returnPressed.connect(self.confirmName)
        
        #this will list the selected objects, but doesn't actually select the object
        #in the scene. This is not the same as selecting the object.
        list = mc.ls(sl=True)
        #This is basically saying for however many objects you select in the scene, 
        #that many will appear in the list.        
        for x in list:                  
            self.myWidget.listSel.addItem(x)
    
    #ALL USER DEFINED FUNCTIONS BELOW
    #All def functions within a class must use "self" to know to look for the 
    #function within the class. If a def function is outside the class, you do not 
    #need "self"
            
    #When listed item is clicked, the object in the scene needs to be selected.
    def listedItem(self, item):
        #does what it says...        
        print item.text()
        #the name (string) of the listed item is stored to a "self.name" variable.
        self.name = item.text()
        #select the object in the scene that has its name selected in the list.
        mc.select(self.name)
                
        
    #When "Alrighty" button is pressed, the name will be changed on object.
    def confirmName(self):
        print self.name
        #rename the object in the scene with whatever the text is in the line edit field.
        mc.rename(self.name, self.myWidget.editName.text())
        
        #change name in list... Think of the '.' between names as namespaces.
        #The selected item in the list is stored to the "selItems" variable.
        selItems = self.myWidget.listSel.selectedItems()
        
        #For each current selection in the list with the selected item, set the text to the 
        #text that is given in the QLineEdit widget which is named "editName" in Qt Designer. 
        for currentSel in selItems:
            currentSel.setText(self.myWidget.editName.text())
            
        
    #Close window
    def exitWin(self):
        self.close()
                

if __name__ == "__main__":
        
    ui = RenamerUI()
    ui.show()

  
