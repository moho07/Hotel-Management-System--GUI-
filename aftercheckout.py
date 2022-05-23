from PyQt5.QtWidgets import QMainWindow
from aftercheckout_ui import Ui_after_checkout


class showprice(QMainWindow, Ui_after_checkout):
    def __init__(self, rent_value):
        super().__init__()

        self.show()
        self.rentvalue.addItem(str(rent_value))