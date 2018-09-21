# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuTesting = QtWidgets.QMenu(self.menubar)
        self.menuTesting.setObjectName("menuTesting")
        self.menuExperiments = QtWidgets.QMenu(self.menubar)
        self.menuExperiments.setObjectName("menuExperiments")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setObjectName("actionOutput")
        self.actionMonitor = QtWidgets.QAction(MainWindow)
        self.actionMonitor.setObjectName("actionMonitor")
        self.actionSound_Video = QtWidgets.QAction(MainWindow)
        self.actionSound_Video.setObjectName("actionSound_Video")
        self.actionTest_Vector_Conversions_Math = QtWidgets.QAction(MainWindow)
        self.actionTest_Vector_Conversions_Math.setObjectName("actionTest_Vector_Conversions_Math")
        self.actionTest_Video_Player = QtWidgets.QAction(MainWindow)
        self.actionTest_Video_Player.setObjectName("actionTest_Video_Player")
        self.actionTest_Continuous_Fluxgate_Monitor = QtWidgets.QAction(MainWindow)
        self.actionTest_Continuous_Fluxgate_Monitor.setObjectName("actionTest_Continuous_Fluxgate_Monitor")
        self.menuTesting.addAction(self.actionOutput)
        self.menuTesting.addAction(self.actionMonitor)
        self.menuTesting.addAction(self.actionSound_Video)
        self.menuTesting.addAction(self.actionTest_Vector_Conversions_Math)
        self.menuTesting.addAction(self.actionTest_Video_Player)
        self.menuTesting.addAction(self.actionTest_Continuous_Fluxgate_Monitor)
        self.menubar.addAction(self.menuTesting.menuAction())
        self.menubar.addAction(self.menuExperiments.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Human Magnetic Reception Experiment"))
        MainWindow.setToolTip(_translate("MainWindow", "HMRE Application"))
        self.menuTesting.setTitle(_translate("MainWindow", "Testing"))
        self.menuExperiments.setTitle(_translate("MainWindow", "Experiments"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionMonitor.setText(_translate("MainWindow", "Monitor"))
        self.actionSound_Video.setText(_translate("MainWindow", "Sound/Video"))
        self.actionTest_Vector_Conversions_Math.setText(_translate("MainWindow", "Test Vector Conversions / Math"))
        self.actionTest_Video_Player.setText(_translate("MainWindow", "Test Video Player"))
        self.actionTest_Continuous_Fluxgate_Monitor.setText(_translate("MainWindow", "Test Continuous Fluxgate Monitor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

