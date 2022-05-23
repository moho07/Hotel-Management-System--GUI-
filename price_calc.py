from PyQt5.QtWidgets import QMainWindow
from price_calc_ui import Ui_price_calc

class price_calc(QMainWindow, Ui_price_calc):
    def __init__(self, hide):
        super().__init__()

        self.pricechanged_label.hide()

        if not hide:
            self.show()

        self.__clicked()

    def __clicked(self):
        self.submit.clicked.connect(lambda: self.__pricesub())

    def __pricesub(self):
        self.pricechanged_label.hide()

        price_file = open('price.txt', 'w')
        price_list = [self.baseprice.text(), self.tax.text()]
        for list in price_list:
            price_file.write('%s\n' % list)
        price_file.close()

        self.pricechanged_label.show()

    def clear(self):
        self.baseprice.clear()
        self.tax.clear()
        self.pricechanged_label.hide()

    