from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_after_checkout(object):
    def __init__(self):
        self.setupUi(self)
        
    def setupUi(self, after_checkout):
        after_checkout.setObjectName("after_checkout")
        after_checkout.resize(516, 268)
        self.centralwidget = QtWidgets.QWidget(after_checkout)
        self.centralwidget.setObjectName("centralwidget")
        self.totalrent_label = QtWidgets.QLabel(self.centralwidget)
        self.totalrent_label.setEnabled(True)
        self.totalrent_label.setGeometry(QtCore.QRect(90, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalrent_label.setFont(font)
        self.totalrent_label.setObjectName("totalrent_label")
        self.rentvalue = QtWidgets.QListWidget(self.centralwidget)
        self.rentvalue.setGeometry(QtCore.QRect(270, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rentvalue.setFont(font)
        self.rentvalue.setObjectName("rentvalue")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(180, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.guestcheckedout_label = QtWidgets.QLabel(self.centralwidget)
        self.guestcheckedout_label.setEnabled(True)
        self.guestcheckedout_label.setGeometry(QtCore.QRect(140, 30, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.guestcheckedout_label.setFont(font)
        self.guestcheckedout_label.setObjectName("guestcheckedout_label")
        after_checkout.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(after_checkout)
        self.statusbar.setObjectName("statusbar")
        after_checkout.setStatusBar(self.statusbar)

        self.retranslateUi(after_checkout)
        QtCore.QMetaObject.connectSlotsByName(after_checkout)

    def retranslateUi(self, after_checkout):
        _translate = QtCore.QCoreApplication.translate
        after_checkout.setWindowTitle(_translate("after_checkout", "MainWindow"))
        self.totalrent_label.setToolTip(_translate("after_checkout", "<html><head/><body><p>Name</p></body></html>"))
        self.totalrent_label.setWhatsThis(_translate("after_checkout", "<html><head/><body><p>Name</p></body></html>"))
        self.totalrent_label.setText(_translate("after_checkout", "Total Rent (Rs.) is:"))
        self.ok.setText(_translate("after_checkout", "OK"))
        self.guestcheckedout_label.setToolTip(_translate("after_checkout", "<html><head/><body><p>Name</p></body></html>"))
        self.guestcheckedout_label.setWhatsThis(_translate("after_checkout", "<html><head/><body><p>Name</p></body></html>"))
        self.guestcheckedout_label.setText(_translate("after_checkout", "Guest Checked Out!"))
