# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TimerUIElement.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 371, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.timerTab = QtWidgets.QWidget()
        self.timerTab.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.timerTab.setToolTip("")
        self.timerTab.setAccessibleName("")
        self.timerTab.setObjectName("timerTab")
        self.layoutWidget = QtWidgets.QWidget(self.timerTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.timerLcd = QtWidgets.QLCDNumber(self.layoutWidget)
        self.timerLcd.setDigitCount(14)
        self.timerLcd.setObjectName("timerLcd")
        self.gridLayout.addWidget(self.timerLcd, 0, 0, 1, 3)
        self.relaxLcd = QtWidgets.QLCDNumber(self.layoutWidget)
        self.relaxLcd.setDigitCount(12)
        self.relaxLcd.setObjectName("relaxLcd")
        self.gridLayout.addWidget(self.relaxLcd, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 3, 1)
        self.learnLcd = QtWidgets.QLCDNumber(self.layoutWidget)
        self.learnLcd.setDigitCount(12)
        self.learnLcd.setObjectName("learnLcd")
        self.gridLayout.addWidget(self.learnLcd, 1, 2, 1, 1)
        self.relaxView = QtWidgets.QColumnView(self.layoutWidget)
        self.relaxView.setObjectName("relaxView")
        self.gridLayout.addWidget(self.relaxView, 2, 0, 1, 1)
        self.columnView = QtWidgets.QColumnView(self.layoutWidget)
        self.columnView.setObjectName("columnView")
        self.gridLayout.addWidget(self.columnView, 2, 2, 1, 1)
        self.relaxPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.relaxPushButton.setObjectName("relaxPushButton")
        self.gridLayout.addWidget(self.relaxPushButton, 3, 0, 1, 1)
        self.learnPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.learnPushButton.setCheckable(False)
        self.learnPushButton.setAutoDefault(True)
        self.learnPushButton.setObjectName("learnPushButton")
        self.gridLayout.addWidget(self.learnPushButton, 3, 2, 1, 1)
        self.tabWidget.addTab(self.timerTab, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.settingTextBrowser = QtWidgets.QTextBrowser(self.settingTab)
        self.settingTextBrowser.setGeometry(QtCore.QRect(10, 10, 341, 241))
        self.settingTextBrowser.setObjectName("settingTextBrowser")
        self.tabWidget.addTab(self.settingTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.learnPushButton.clicked.connect(self.learnLcd.setHexMode)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        self.relaxPushButton.setText(_translate("MainWindow", "relax"))
        self.learnPushButton.setText(_translate("MainWindow", "learn"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.timerTab), _translate("MainWindow", "Timer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab), _translate("MainWindow", "Settings"))

