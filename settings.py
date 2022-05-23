import windows
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget)
from settings_ui import Ui_settings

class settings(QMainWindow, Ui_settings):
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
        self.pricecalc.clicked.connect(lambda: self.__openwindow(windows.pricecalc_window))
        self.addrooms.clicked.connect(lambda: self.__openwindow(windows.addrooms_window))
        self.removerooms.clicked.connect(lambda: self.__openwindow(windows.removerooms_window))
    
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