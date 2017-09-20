import maya.cmds as mc
import sys
import maya.OpenMayaUI as mui
from PySide import QtCore, QtGui, QtUiTools
import shiboken

####################    Renamer v 1.0 by Michelle Hill   ####################
###########Before running, add file path to the location of the .ui file#####

#Imports .ui file
class RenamerUI(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("C:\Add path to .ui file here")#ADD YOUR FILE PATH HERE!
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self)
        self.myWidget.listSel.itemClicked.connect(self.listedItem)
        self.myWidget.listSel.itemClicked.connect(self.updateRename)
        self.myWidget.closeBttn.clicked.connect(self.exitWin)
        self.myWidget.editName.returnPressed.connect(self.confirmName)
        self.myWidget.updateBttn.clicked.connect(self.updateList)
        self.myWidget.preBttn.clicked.connect(self.addPre)
        self.myWidget.suffBttn.clicked.connect(self.addSuf)

    #Qt Widget functions below
    def listedItem(self, item):
        self.name = item.text()
        mc.select(self.name)

    def updateList(self):
        self.myWidget.listSel.clear()
        list = mc.ls(sl=True)
        for x in list:
            self.myWidget.listSel.addItem(x)

    def confirmName(self):
        mc.rename(self.name, self.myWidget.editName.text())
        selItems = self.myWidget.listSel.selectedItems()
        for currentSel in selItems:
            currentSel.setText(self.myWidget.editName.text())

    def updateRename(self):
        self.myWidget.editName.setText(self.name)

    def addPre(self):
        editStr = self.myWidget.listSel.selectedItems()
        prefix = self.myWidget.preEdit.text()
        for add in editStr:
            mc.rename(prefix + self.name)
            add.setText(prefix + self.name)

    def addSuf(self):
        editStr2 = self.myWidget.listSel.selectedItems()
        suffix = self.myWidget.suffEdit.text()
        for add in editStr2:
            mc.rename(self.name + suffix)
            add.setText(self.name + suffix)

    def exitWin(self):
        self.close()
        print "Renamer 1.0 was closed."


if __name__ == "__main__":
    ui = RenamerUI()
    ui.show()



