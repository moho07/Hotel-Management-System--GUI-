import sys
sys.path.insert(1, 'D:\College\Projects\Python\Hotel Management System (GUI)\GUIs (Python Files)')
import windows
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDesktopWidget)
from welcome_screen_ui import Ui_MainWindow

app = QApplication(sys.argv)

class welcome_screen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        windows.init()
        
        self.center()
        self.show()
        self.__clicked()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def __clicked(self):
        self.reservation.clicked.connect(lambda: self.__openwindow(windows.reserve_window))
        self.checkin.clicked.connect(lambda: self.__openwindow(windows.checkin_window))
        self.checkout.clicked.connect(lambda: self.__openwindow(windows.checkout_window))
        self.guestlist.clicked.connect(lambda: self.__openwindow(windows.guestlist_window))
        self.settings.clicked.connect(lambda: self.__openwindow(windows.settings_window))
        self.exit.clicked.connect(self.close)

    def __openwindow(self, window):
        self.hide()
        window.show()
        window.back.clicked.connect(lambda: self.__goback(window))
  
    def __goback(self, window):
        window.hide()
        window.clear()
        self.show()

welc = welcome_screen()

sys.exit(app.exec())