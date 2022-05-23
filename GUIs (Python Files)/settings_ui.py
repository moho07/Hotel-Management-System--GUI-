from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def __init__(self):
        self.setupUi(self)

    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(515, 750)
        self.centralwidget = QtWidgets.QWidget(settings)
        self.centralwidget.setObjectName("centralwidget")
        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(180, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.settings_label.setFont(font)
        self.settings_label.setObjectName("settings_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(170, 630, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.pricecalc = QtWidgets.QPushButton(self.centralwidget)
        self.pricecalc.setGeometry(QtCore.QRect(80, 110, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pricecalc.setFont(font)
        self.pricecalc.setObjectName("pricecalc")
        self.addrooms = QtWidgets.QPushButton(self.centralwidget)
        self.addrooms.setGeometry(QtCore.QRect(80, 280, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addrooms.setFont(font)
        self.addrooms.setObjectName("addrooms")
        self.removerooms = QtWidgets.QPushButton(self.centralwidget)
        self.removerooms.setGeometry(QtCore.QRect(80, 450, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.removerooms.setFont(font)
        self.removerooms.setObjectName("removerooms")
        settings.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(settings)
        self.statusbar.setObjectName("statusbar")
        settings.setStatusBar(self.statusbar)

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "MainWindow"))
        self.settings_label.setText(_translate("settings", "Settings"))
        self.back.setText(_translate("settings", "Back"))
        self.pricecalc.setText(_translate("settings", "Price Calculation"))
        self.addrooms.setText(_translate("settings", "Add Rooms"))
        self.removerooms.setText(_translate("settings", "Remove Rooms"))
