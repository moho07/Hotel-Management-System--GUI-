from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_show_bookingid(object):
    def __init__(self):
        self.setupUi(self)
        
    def setupUi(self, show_bookingid):
        show_bookingid.setObjectName("show_bookingid")
        show_bookingid.resize(516, 263)
        self.centralwidget = QtWidgets.QWidget(show_bookingid)
        self.centralwidget.setObjectName("centralwidget")
        self.yourbookingid_label = QtWidgets.QLabel(self.centralwidget)
        self.yourbookingid_label.setEnabled(True)
        self.yourbookingid_label.setGeometry(QtCore.QRect(70, 80, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yourbookingid_label.setFont(font)
        self.yourbookingid_label.setObjectName("yourbookingid_label")
        self.checkin = QtWidgets.QPushButton(self.centralwidget)
        self.checkin.setGeometry(QtCore.QRect(280, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkin.setFont(font)
        self.checkin.setObjectName("checkin")
        self.bookingidvalue = QtWidgets.QListWidget(self.centralwidget)
        self.bookingidvalue.setGeometry(QtCore.QRect(260, 80, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bookingidvalue.setFont(font)
        self.bookingidvalue.setObjectName("bookingidvalue")
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(80, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        show_bookingid.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(show_bookingid)
        self.statusbar.setObjectName("statusbar")
        show_bookingid.setStatusBar(self.statusbar)

        self.retranslateUi(show_bookingid)
        QtCore.QMetaObject.connectSlotsByName(show_bookingid)

    def retranslateUi(self, show_bookingid):
        _translate = QtCore.QCoreApplication.translate
        show_bookingid.setWindowTitle(_translate("show_bookingid", "MainWindow"))
        self.yourbookingid_label.setToolTip(_translate("show_bookingid", "<html><head/><body><p>Name</p></body></html>"))
        self.yourbookingid_label.setWhatsThis(_translate("show_bookingid", "<html><head/><body><p>Name</p></body></html>"))
        self.yourbookingid_label.setText(_translate("show_bookingid", "Your Booking ID is: "))
        self.checkin.setText(_translate("show_bookingid", "Check In"))
        self.ok.setText(_translate("show_bookingid", "OK"))
