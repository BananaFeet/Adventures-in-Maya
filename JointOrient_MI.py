# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JointOrient_MI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainUI(QtGui.QMainWindow):
    def setupUi(self, MainUI):
        MainUI.setObjectName(_fromUtf8("MainUI"))
        MainUI.resize(389, 214)
        MainUI.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainUI.setAutoFillBackground(False)
        #MainUI.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Lra_Bttn = QtGui.QPushButton(self.centralwidget)
        self.Lra_Bttn.setGeometry(QtCore.QRect(30, 20, 91, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Lra_Bttn.sizePolicy().hasHeightForWidth())
        self.Lra_Bttn.setSizePolicy(sizePolicy)
        self.Lra_Bttn.setObjectName(_fromUtf8("Lra_Bttn"))
        self.Aim_lbl = QtGui.QLabel(self.centralwidget)
        self.Aim_lbl.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.Aim_lbl.setObjectName(_fromUtf8("Aim_lbl"))
        self.Up_lbl = QtGui.QLabel(self.centralwidget)
        self.Up_lbl.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.Up_lbl.setObjectName(_fromUtf8("Up_lbl"))
        self.Invert_lbl1 = QtGui.QLabel(self.centralwidget)
        self.Invert_lbl1.setGeometry(QtCore.QRect(290, 70, 81, 31))
        self.Invert_lbl1.setObjectName(_fromUtf8("Invert_lbl1"))
        self.Invert_lbl2 = QtGui.QLabel(self.centralwidget)
        self.Invert_lbl2.setGeometry(QtCore.QRect(290, 110, 81, 31))
        self.Invert_lbl2.setObjectName(_fromUtf8("Invert_lbl2"))
        self.SelHiearch_bttn = QtGui.QPushButton(self.centralwidget)
        self.SelHiearch_bttn.setGeometry(QtCore.QRect(150, 20, 91, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelHiearch_bttn.sizePolicy().hasHeightForWidth())
        self.SelHiearch_bttn.setSizePolicy(sizePolicy)
        self.SelHiearch_bttn.setObjectName(_fromUtf8("SelHiearch_bttn"))
        self.Xaim_radio = QtGui.QRadioButton(self.centralwidget)
        self.Xaim_radio.setGeometry(QtCore.QRect(140, 75, 31, 21))
        self.Xaim_radio.setObjectName(_fromUtf8("Xaim_radio"))
        self.Xup_radio = QtGui.QRadioButton(self.centralwidget)
        self.Xup_radio.setGeometry(QtCore.QRect(140, 115, 31, 21))
        self.Xup_radio.setObjectName(_fromUtf8("Xup_radio"))
        self.Yaim_radio = QtGui.QRadioButton(self.centralwidget)
        self.Yaim_radio.setGeometry(QtCore.QRect(190, 75, 31, 21))
        self.Yaim_radio.setObjectName(_fromUtf8("Yaim_radio"))
        self.Yup_radio = QtGui.QRadioButton(self.centralwidget)
        self.Yup_radio.setGeometry(QtCore.QRect(190, 115, 31, 21))
        self.Yup_radio.setObjectName(_fromUtf8("Yup_radio"))
        self.Zaim_radio = QtGui.QRadioButton(self.centralwidget)
        self.Zaim_radio.setGeometry(QtCore.QRect(240, 75, 31, 21))
        self.Zaim_radio.setObjectName(_fromUtf8("Zaim_radio"))
        self.Zup_radio = QtGui.QRadioButton(self.centralwidget)
        self.Zup_radio.setGeometry(QtCore.QRect(240, 115, 31, 21))
        self.Zup_radio.setObjectName(_fromUtf8("Zup_radio"))
        self.checkBox_1 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(360, 70, 21, 31))
        self.checkBox_1.setObjectName(_fromUtf8("checkBox_1"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(360, 110, 21, 31))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.Orient_bttn = QtGui.QPushButton(self.centralwidget)
        self.Orient_bttn.setGeometry(QtCore.QRect(130, 150, 121, 41))
        self.Orient_bttn.setStyleSheet(_fromUtf8("background-color: rgb(3, 132, 117);\n"
"color: rgb(255, 255, 255);"))
        self.Orient_bttn.setObjectName(_fromUtf8("Orient_bttn"))
        self.ZeroJnts_bttn = QtGui.QPushButton(self.centralwidget)
        self.ZeroJnts_bttn.setGeometry(QtCore.QRect(260, 20, 91, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZeroJnts_bttn.sizePolicy().hasHeightForWidth())
        self.ZeroJnts_bttn.setSizePolicy(sizePolicy)
        self.ZeroJnts_bttn.setObjectName(_fromUtf8("ZeroJnts_bttn"))
        self.frame1 = QtGui.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(10, 70, 371, 31))
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName(_fromUtf8("frame1"))
        self.frame2 = QtGui.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(10, 109, 371, 31))
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setObjectName(_fromUtf8("frame2"))
        MainUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainUI.setStatusBar(self.statusbar)

        self.retranslateUi(MainUI)
        QtCore.QMetaObject.connectSlotsByName(MainUI)

    def retranslateUi(self, MainUI):
        MainUI.setWindowTitle(_translate("MainUI", "Joint Orient Tool - v 1.0", None))
        self.Lra_Bttn.setText(_translate("MainUI", "Toggle Local Axis", None))
        self.Aim_lbl.setText(_translate("MainUI", "Aim Axis (Primary):", None))
        self.Up_lbl.setText(_translate("MainUI", "Up Axis (Secondary):", None))
        self.Invert_lbl1.setText(_translate("MainUI", "Invert Axis:", None))
        self.Invert_lbl2.setText(_translate("MainUI", "Invert Axis:", None))
        self.SelHiearch_bttn.setText(_translate("MainUI", "Select Hiearchy", None))
        self.Xaim_radio.setText(_translate("MainUI", "X", None))
        self.Xup_radio.setText(_translate("MainUI", "X", None))
        self.Yaim_radio.setText(_translate("MainUI", "Y", None))
        self.Yup_radio.setText(_translate("MainUI", "Y", None))
        self.Zaim_radio.setText(_translate("MainUI", "Z", None))
        self.Zup_radio.setText(_translate("MainUI", "Z", None))
        self.checkBox_1.setText(_translate("MainUI", " ", None))
        self.Orient_bttn.setText(_translate("MainUI", "Orient Joints!", None))
        self.ZeroJnts_bttn.setText(_translate("MainUI", "Zero Joint(s)", None))

if __name__ == "__main__":
    # Set up application with any command line args
    app = QtGui.QApplication(sys.argv)
    MainWindow = Ui_MainUI()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()