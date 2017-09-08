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
        self.myWidget.listSel.itemClicked.connect(self.updateRename)
        self.myWidget.closeBttn.clicked.connect(self.exitWin)
        self.myWidget.editName.returnPressed.connect(self.confirmName)
        self.myWidget.updateBttn.clicked.connect(self.updateList)
        #self.myWidget.addPrefix.stateChanged.connect(self.Prefix)    
        
    #ALL USER DEFINED FUNCTIONS BELOW**
    #All def functions within a class must use "self" to know to look for the 
    #function within the class. If a def function is outside the class, you do not 
    #need "self"
    
    #FUNCTION FOR LIST WIDGET        
    #When listed item is clicked, the object in the scene needs to be selected.
    def listedItem(self, item):              
        #the name (string) of the listed item is stored to a "self.name" variable.
        self.name = item.text()
        #select the object in the scene that has its name selected in the list.
        mc.select(self.name)
        
    #FUNCTION TO UPDATE LIST WIDGET
    def updateList(self):
        #Before the selection is listed, clear the list...
        self.myWidget.listSel.clear()
        #this will list the selected objects, but doesn't actually select the object
        #in the scene. This is not the same as selecting the object.  
        list = mc.ls(sl=True)        
        #This is basically saying for however many objects you select in the scene, 
        #that many will appear in the list.  
        for x in list:                                        
            self.myWidget.listSel.addItem(x)
       
                               
    #FUNCTION FOR QLINE EDIT FOR RENAMING    
    #When the "Enter" key is pressed, the name will be changed on object.
    def confirmName(self):
        #rename the object in the scene with whatever the text is in the line edit field.
        mc.rename(self.name, self.myWidget.editName.text())       
        #change name in list... Think of the '.' between names as namespaces.
        #The selected item in the list is stored to the "selItems" variable.
        selItems = self.myWidget.listSel.selectedItems()        
        #For each current selection in the list with the selected item, set the text to the 
        #text that is given in the QLineEdit widget which is named "editName" in Qt Designer. 
        for currentSel in selItems:
            currentSel.setText(self.myWidget.editName.text())
                       
    #Rename text field gets updated with whatever is selected
    def updateRename(self):
        #This literally says "hey, set my line edit to the name of the selection." The name
        #of the selection is self.name which has the listed items stored into that variable.
        #holy shit...IT WORKS       
        self.myWidget.editName.setText(self.name)
               
#FUNCTION FOR ADD PREFIX QLINE EDIT
#Add prefix to selection
    
    
    #Take current name and just add a Prefix if box is checked
    #def Prefix(self):
        #if the box is checked these are the conditions. 
        #Remember you have to add "myWidget" so it can know if you are referring to any 
        #parts of the gui. If you don't, it will not recognize it as an attribute.
        #if self.myWidget.addPrefix.isChecked():
            
            #This works...now make it add a prefix to a given name...
            #print "CHECK MATE!"
        #else:
            #print "Nope"
           
    #Close window
    def exitWin(self):
        self.close()
        #remember who you talking to!
        print "Michelle's GUI has closed!"
                

if __name__ == "__main__":
        
    ui = RenamerUI()
    ui.show()

  
