import sql_connect
from PyQt5.QtWidgets import QMainWindow
from checkout_ui import Ui_checkout
from aftercheckout import showprice

class checkout(QMainWindow, Ui_checkout):
    def __init__(self, hide):
        super().__init__()
        
        self.guestidnotfound_label.hide()

        if not hide:
            self.show()

        self.__clicked()

    def __clicked(self):
        self.guest_submit.clicked.connect(lambda: self.__guestid_sub())
    
    def __guestid_sub(self):
        self.guestidnotfound_label.hide()

        guest_id_text = self.guestid.text()

        sql_exec = 'SELECT* FROM guest_list WHERE guest_id = %s AND status = 1'
        sql_arg = (guest_id_text)

        sql_connect.sql.cursor.execute(sql_exec, sql_arg)
        row = sql_connect.sql.cursor.fetchall()

        if len(row) == 0:
            self.guestidnotfound_label.show()
        else:
            sql_exec = 'UPDATE guest_list SET status = 0 WHERE guest_id = %s'

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)

            sql_exec = 'UPDATE rooms_list SET status = 0 WHERE room_no IN (SELECT room_no FROM guest_list WHERE guest_id = %s)'

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            sql_connect.sql.connect.commit()

            sql_exec = 'SELECT DATEDIFF(checkin, checkout) FROM guest_list WHERE guest_id = %s'
            
            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            days = sql_connect.sql.cursor.fetchone()

            price_file = open('price.txt', 'r')
            price_list =  [current_place.rstrip() for current_place in price_file.readlines()]
            rent = int(price_list[0])*int(days[0]) + int(price_list[1])*(int(price_list[0])*int(days[0]))

            self.hide()
            self.rent_window = showprice(rent)

            self.rent_window.ok.clicked.connect(lambda: self.__openwindow())
    
    def __openwindow(self):
        self.rent_window.close()
        self.clear()
        self.show()

    def clear(self):
        self.guestid.clear()
        self.guestidnotfound_label.hide()