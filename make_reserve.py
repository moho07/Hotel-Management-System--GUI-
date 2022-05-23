import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)

from make_reserve_ui import Ui_Reservation

app = QApplication(sys.argv)



class make_reserve(QMainWindow, Ui_Reservation):
    def __init__(self):
        super().__init__()
        self.show()
        self.__clicked()
    
    def __get_info(self):
        pass

    def __go_back(self):
        pass
    
    def __clicked(self):
        self.submit.clicked.connect(self.__get_info())
        self.cancel.clicked.connect(lambda: self.__go_back(self))


make_reserve_window = make_reserve()
sys.exit(app.exec())