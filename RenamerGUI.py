# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Renamer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, uic
import sys


class Ui_MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        uic.loadUi("Renamer.ui", self)

#Make the button work!
    @QtCore.pyqtSlot(name='on_OKbttn_pressed')
    def buttonclicked(self):
        print "HELLO"
        self.textEdit.setText("stuff")
if __name__ == "__main__":
    # Set up application with any command line args
    app = QtGui.QApplication(sys.argv)

    ui = Ui_MainWindow()

    ui.show()

    # Lastly, when we are done... EXIT
    sys.exit(app.exec_())


