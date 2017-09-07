import maya.cmds as mc
import sys
from PySide import QtCore, QtGui, QtUiTools


class RenamerUI(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("C:\Users\michelle.hill\PycharmProjects\Learning\Renamer.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self)

        #Add button functions


        file.close()


#MAYA FUNCTIONS BELOW...


#Selection will add more text fields


if __name__ == "__main__":
    # Set up application with any command line args
    #app = QtGui.QApplication(sys.argv)

    ui = RenamerUI()

    ui.show()

    # Lastly, when we are done... EXIT
    #sys.exit(app.exec_())
