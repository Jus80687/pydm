# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pydm.ui'
#
# Created: Wed Sep 30 13:44:51 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(672, 112)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.panelSearchLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.panelSearchLineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.panelSearchLineEdit.setObjectName(_fromUtf8("panelSearchLineEdit"))
        self.horizontalLayout.addWidget(self.panelSearchLineEdit)
        self.goButton = QtGui.QPushButton(self.centralwidget)
        self.goButton.setFlat(False)
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.horizontalLayout.addWidget(self.goButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.backButton = QtGui.QPushButton(self.centralwidget)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.forwardButton = QtGui.QPushButton(self.centralwidget)
        self.forwardButton.setObjectName(_fromUtf8("forwardButton"))
        self.horizontalLayout.addWidget(self.forwardButton)
        self.homeButton = QtGui.QPushButton(self.centralwidget)
        self.homeButton.setObjectName(_fromUtf8("homeButton"))
        self.horizontalLayout.addWidget(self.homeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit_in_Designer = QtGui.QAction(MainWindow)
        self.actionEdit_in_Designer.setObjectName(_fromUtf8("actionEdit_in_Designer"))
        self.actionAbout_DIM = QtGui.QAction(MainWindow)
        self.actionAbout_DIM.setEnabled(False)
        self.actionAbout_DIM.setObjectName(_fromUtf8("actionAbout_DIM"))
        self.actionReload_Display = QtGui.QAction(MainWindow)
        self.actionReload_Display.setObjectName(_fromUtf8("actionReload_Display"))
        self.actionIncrease_Font_Size = QtGui.QAction(MainWindow)
        self.actionIncrease_Font_Size.setObjectName(_fromUtf8("actionIncrease_Font_Size"))
        self.actionDecrease_Font_Size = QtGui.QAction(MainWindow)
        self.actionDecrease_Font_Size.setObjectName(_fromUtf8("actionDecrease_Font_Size"))
        self.menuFile.addAction(self.actionAbout_DIM)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEdit_in_Designer)
        self.menuFile.addAction(self.actionReload_Display)
        self.menuView.addAction(self.actionIncrease_Font_Size)
        self.menuView.addAction(self.actionDecrease_Font_Size)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyDM Main Window", None))
        self.panelSearchLineEdit.setPlaceholderText(_translate("MainWindow", "Search for a display...", None))
        self.goButton.setText(_translate("MainWindow", "Go", None))
        self.backButton.setText(_translate("MainWindow", "Back", None))
        self.forwardButton.setText(_translate("MainWindow", "Forward", None))
        self.homeButton.setText(_translate("MainWindow", "Home", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionEdit_in_Designer.setText(_translate("MainWindow", "Edit in Designer", None))
        self.actionAbout_DIM.setText(_translate("MainWindow", "About PyDM", None))
        self.actionReload_Display.setText(_translate("MainWindow", "Reload Display", None))
        self.actionReload_Display.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionIncrease_Font_Size.setText(_translate("MainWindow", "Increase Font Size", None))
        self.actionIncrease_Font_Size.setShortcut(_translate("MainWindow", "Ctrl+=", None))
        self.actionDecrease_Font_Size.setText(_translate("MainWindow", "Decrease Font Size", None))
        self.actionDecrease_Font_Size.setShortcut(_translate("MainWindow", "Ctrl+-", None))

