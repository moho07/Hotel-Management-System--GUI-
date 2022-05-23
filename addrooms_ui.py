from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addrooms(object):
    def __init__(self):
        self.setupUi(self)
        
    def setupUi(self, addrooms):
        addrooms.setObjectName("addrooms")
        addrooms.resize(515, 545)
        self.centralwidget = QtWidgets.QWidget(addrooms)
        self.centralwidget.setObjectName("centralwidget")
        self.addrooms_label = QtWidgets.QLabel(self.centralwidget)
        self.addrooms_label.setGeometry(QtCore.QRect(170, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.addrooms_label.setFont(font)
        self.addrooms_label.setObjectName("addrooms_label")
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
        addrooms.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addrooms)
        self.statusbar.setObjectName("statusbar")
        addrooms.setStatusBar(self.statusbar)

        self.retranslateUi(addrooms)
        QtCore.QMetaObject.connectSlotsByName(addrooms)

    def retranslateUi(self, addrooms):
        _translate = QtCore.QCoreApplication.translate
        addrooms.setWindowTitle(_translate("addrooms", "MainWindow"))
        self.addrooms_label.setText(_translate("addrooms", "Add Rooms"))
        self.back.setText(_translate("addrooms", "Back"))
        self.rooms_list.setText(_translate("addrooms", "Room List"))
        self.roomtype.setText(_translate("addrooms", "Room Type"))
