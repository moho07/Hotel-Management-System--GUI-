from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_removerooms(object):
    def __init__(self):
        self.setupUi(self)
        
    def setupUi(self, removerooms):
        removerooms.setObjectName("removerooms")
        removerooms.resize(515, 545)
        self.centralwidget = QtWidgets.QWidget(removerooms)
        self.centralwidget.setObjectName("centralwidget")
        self.removerooms_label = QtWidgets.QLabel(self.centralwidget)
        self.removerooms_label.setGeometry(QtCore.QRect(130, 30, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.removerooms_label.setFont(font)
        self.removerooms_label.setObjectName("removerooms_label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(170, 450, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.rooms_list = QtWidgets.QPushButton(self.centralwidget)
        self.rooms_list.setGeometry(QtCore.QRect(80, 110, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rooms_list.setFont(font)
        self.rooms_list.setObjectName("rooms_list")
        self.roomtype = QtWidgets.QPushButton(self.centralwidget)
        self.roomtype.setGeometry(QtCore.QRect(80, 280, 341, 131))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.roomtype.setFont(font)
        self.roomtype.setObjectName("roomtype")
        removerooms.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(removerooms)
        self.statusbar.setObjectName("statusbar")
        removerooms.setStatusBar(self.statusbar)

        self.retranslateUi(removerooms)
        QtCore.QMetaObject.connectSlotsByName(removerooms)

    def retranslateUi(self, removerooms):
        _translate = QtCore.QCoreApplication.translate
        removerooms.setWindowTitle(_translate("removerooms", "MainWindow"))
        self.removerooms_label.setText(_translate("removerooms", "Remove Rooms"))
        self.back.setText(_translate("removerooms", "Back"))
        self.rooms_list.setText(_translate("removerooms", "Room List"))
        self.roomtype.setText(_translate("removerooms", "Room Type"))
