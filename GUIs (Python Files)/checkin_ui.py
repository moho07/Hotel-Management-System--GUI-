from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_checkin(object):
    def __init__(self):
        self.setupUi(self)

    def setupUi(self, checkin):
        checkin.setObjectName("checkin")
        checkin.resize(516, 411)
        self.centralwidget = QtWidgets.QWidget(checkin)
        self.centralwidget.setObjectName("centralwidget")
        self.checkin_label = QtWidgets.QLabel(self.centralwidget)
        self.checkin_label.setGeometry(QtCore.QRect(190, 30, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.checkin_label.setFont(font)
        self.checkin_label.setObjectName("checkin_label")
        self.select_roomno = QtWidgets.QComboBox(self.centralwidget)
        self.select_roomno.setEnabled(True)
        self.select_roomno.setGeometry(QtCore.QRect(270, 250, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.select_roomno.setFont(font)
        self.select_roomno.setObjectName("select_roomno")
        self.select_roomno.addItem("")
        self.select_room_label = QtWidgets.QLabel(self.centralwidget)
        self.select_room_label.setEnabled(True)
        self.select_room_label.setGeometry(QtCore.QRect(80, 250, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.select_room_label.setFont(font)
        self.select_room_label.setObjectName("select_room_label")
        self.room_submit = QtWidgets.QPushButton(self.centralwidget)
        self.room_submit.setEnabled(True)
        self.room_submit.setGeometry(QtCore.QRect(170, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.room_submit.setFont(font)
        self.room_submit.setObjectName("room_submit")
        self.bookingnotfound_label = QtWidgets.QLabel(self.centralwidget)
        self.bookingnotfound_label.setEnabled(True)
        self.bookingnotfound_label.setGeometry(QtCore.QRect(10, 230, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bookingnotfound_label.setFont(font)
        self.bookingnotfound_label.setObjectName("bookingnotfound_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(280, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.booking_submit = QtWidgets.QPushButton(self.centralwidget)
        self.booking_submit.setGeometry(QtCore.QRect(80, 170, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.booking_submit.setFont(font)
        self.booking_submit.setObjectName("booking_submit")
        self.roomnonotfound_label = QtWidgets.QLabel(self.centralwidget)
        self.roomnonotfound_label.setEnabled(True)
        self.roomnonotfound_label.setGeometry(QtCore.QRect(10, 290, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.roomnonotfound_label.setFont(font)
        self.roomnonotfound_label.setObjectName("roomnonotfound_label")
        self.guestcheckedin_label = QtWidgets.QLabel(self.centralwidget)
        self.guestcheckedin_label.setEnabled(True)
        self.guestcheckedin_label.setGeometry(QtCore.QRect(10, 290, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.guestcheckedin_label.setFont(font)
        self.guestcheckedin_label.setObjectName("guestcheckedin_label")
        self.booking_Id = QtWidgets.QLineEdit(self.centralwidget)
        self.booking_Id.setGeometry(QtCore.QRect(130, 110, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.booking_Id.setFont(font)
        self.booking_Id.setObjectName("booking_Id")
        self.guestalreadycheckedin_label = QtWidgets.QLabel(self.centralwidget)
        self.guestalreadycheckedin_label.setEnabled(True)
        self.guestalreadycheckedin_label.setGeometry(QtCore.QRect(10, 230, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.guestalreadycheckedin_label.setFont(font)
        self.guestalreadycheckedin_label.setObjectName("guestalreadycheckedin_label")
        checkin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(checkin)
        self.statusbar.setObjectName("statusbar")
        checkin.setStatusBar(self.statusbar)

        self.retranslateUi(checkin)
        QtCore.QMetaObject.connectSlotsByName(checkin)

    def retranslateUi(self, checkin):
        _translate = QtCore.QCoreApplication.translate
        checkin.setWindowTitle(_translate("checkin", "MainWindow"))
        self.checkin_label.setText(_translate("checkin", "Check In"))
        self.select_roomno.setPlaceholderText(_translate("checkin", "Room Type"))
        self.select_roomno.setItemText(0, _translate("checkin", "Select"))
        self.select_room_label.setToolTip(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.select_room_label.setWhatsThis(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.select_room_label.setText(_translate("checkin", "Select Room Number:"))
        self.room_submit.setText(_translate("checkin", "Submit"))
        self.bookingnotfound_label.setToolTip(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.bookingnotfound_label.setWhatsThis(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.bookingnotfound_label.setText(_translate("checkin", "Booking ID not Found! Please try Again"))
        self.back.setText(_translate("checkin", "Cancel"))
        self.booking_submit.setText(_translate("checkin", "Submit"))
        self.roomnonotfound_label.setToolTip(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.roomnonotfound_label.setWhatsThis(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.roomnonotfound_label.setText(_translate("checkin", "Please Select Room No.!"))
        self.guestcheckedin_label.setToolTip(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.guestcheckedin_label.setWhatsThis(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.guestcheckedin_label.setText(_translate("checkin", "Guest has been Checked In!"))
        self.booking_Id.setPlaceholderText(_translate("checkin", "                Booking Id"))
        self.guestalreadycheckedin_label.setToolTip(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.guestalreadycheckedin_label.setWhatsThis(_translate("checkin", "<html><head/><body><p>Name</p></body></html>"))
        self.guestalreadycheckedin_label.setText(_translate("checkin", "Guest Already Checked In!"))
