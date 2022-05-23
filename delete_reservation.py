import sql_connect
from PyQt5.QtWidgets import QMainWindow
from delete_reservation_ui import Ui_delete_reservation

class delete_reserve(QMainWindow, Ui_delete_reservation):
    def __init__(self, hide):
        super().__init__()

        if not hide:
            self.show()

        self.bookingid_notfound_label.hide()
        self.reservationdeleted_label.hide()

        self.__clicked()
    
    def __clicked(self):
        self.bookingsubmit.clicked.connect(lambda: self.__infosubmit())

    def __infosubmit(self):
        self.bookingid_notfound_label.hide()
        self.reservationdeleted_label.hide()
        
        booking_id_text = self.bookingid.text()

        sql_exec = 'SELECT* FROM reservation_list WHERE booking_id = %s'
        sql_arg = (booking_id_text)

        sql_connect.sql.cursor.execute(sql_exec, sql_arg)
        row = sql_connect.sql.cursor.fetchall()

        if len(row) == 0:
            self.bookingid_notfound_label.show()
        else:
            sql_exec = 'DELETE FROM reservation_list WHERE booking_id = %s'
            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            sql_connect.sql.connect.commit()
            self.reservationdeleted_label.show()

    def clear(self):
        self.bookingid.clear()
        self.bookingid_notfound_label.hide()
        self.reservationdeleted_label.hide()
        