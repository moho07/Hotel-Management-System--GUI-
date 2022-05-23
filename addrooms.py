import windows
from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget)
from addrooms_ui import Ui_addrooms

class addrooms(QMainWindow, Ui_addrooms):
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
        self.rooms_list.clicked.connect(lambda: self.__openwindow(windows.addroom_list_window))
        self.roomtype.clicked.connect(lambda: self.__openwindow(windows.addroom_type_window))
    
    def __openwindow(self, window):
        self.hide()
        window.refresh()
        window.show()
        window.back.clicked.connect(lambda: self.__goback(window))
    
    def __goback(self, window):
        window.hide()
        window.clear()
        self.show()

    def clear(self):
        pass