from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reservation(object):
    def __init__(self):
        self.setupUi(self)

    def setupUi(self, reservation_ui):
        reservation_ui.setObjectName("reservation_ui")
        reservation_ui.resize(515, 750)
        font = QtGui.QFont()
        font.setPointSize(20)
        reservation_ui.setFont(font)
        self.centralwidget = QtWidgets.QWidget(reservation_ui)
        self.centralwidget.setObjectName("centralwidget")
        self.make_reservation = QtWidgets.QPushButton(self.centralwidget)
        self.make_reservation.setGeometry(QtCore.QRect(90, 120, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.make_reservation.setFont(font)
        self.make_reservation.setObjectName("make_reservation")
        self.delete_reservation = QtWidgets.QPushButton(self.centralwidget)
        self.delete_reservation.setGeometry(QtCore.QRect(90, 290, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delete_reservation.setFont(font)
        self.delete_reservation.setObjectName("delete_reservation")
        self.search_reservation = QtWidgets.QPushButton(self.centralwidget)
        self.search_reservation.setGeometry(QtCore.QRect(90, 460, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search_reservation.setFont(font)
        self.search_reservation.setObjectName("search_reservation")
        self.reservation_label = QtWidgets.QLabel(self.centralwidget)
        self.reservation_label.setGeometry(QtCore.QRect(170, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.reservation_label.setFont(font)
        self.reservation_label.setObjectName("reservation_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(180, 640, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setObjectName("back")
        reservation_ui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(reservation_ui)
        self.statusbar.setObjectName("statusbar")
        reservation_ui.setStatusBar(self.statusbar)

        self.retranslateUi(reservation_ui)
        QtCore.QMetaObject.connectSlotsByName(reservation_ui)

    def retranslateUi(self, reservation_ui):
        _translate = QtCore.QCoreApplication.translate
        reservation_ui.setWindowTitle(_translate("reservation_ui", "MainWindow"))
        self.make_reservation.setText(_translate("reservation_ui", "Make Reservation"))
        self.delete_reservation.setText(_translate("reservation_ui", "Delete Reservation"))
        self.search_reservation.setText(_translate("reservation_ui", "Search Reservation"))
        self.reservation_label.setText(_translate("reservation_ui", "Reservation"))
        self.back.setText(_translate("reservation_ui", "Back"))
