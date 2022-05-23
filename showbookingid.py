from PyQt5.QtWidgets import QMainWindow
from showbookingid_ui import Ui_show_bookingid


class showbookingid(QMainWindow, Ui_show_bookingid):
    def __init__(self, booking_id):
        super().__init__()

        self.show()
        self.bookingidvalue.addItem(booking_id)

        
    