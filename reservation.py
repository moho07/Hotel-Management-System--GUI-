import windows
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget)
from reservation_ui import Ui_reservation

class reserve(QMainWindow, Ui_reservation):
    def __init__(self, hide):
        super().__init__()
        
        self.center()
        
        if not hide:
            self.show()

        self.__clicked()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def __clicked(self):
        self.make_reservation.clicked.connect(lambda: self.__openwindow(windows.make_reservation_window))
        self.delete_reservation.clicked.connect(lambda: self.__openwindow(windows.delete_reservation_window))
        self.search_reservation.clicked.connect(lambda: self.__openwindow(windows.search_reservation_window))
    
    def __openwindow(self, window):
        self.hide()
        window.show()
        window.back.clicked.connect(lambda: self.__goback(window))
    
    def __goback(self, window):
        window.hide()
        window.clear()
        self.show()

    def clear(self):
        pass