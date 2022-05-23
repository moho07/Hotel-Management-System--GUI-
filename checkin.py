import sql_connect
from PyQt5.QtWidgets import QMainWindow
from checkin_ui import Ui_checkin

class checkin(QMainWindow, Ui_checkin):
    def __init__(self, hide):
        super().__init__()

        self.select_roomno.hide()
        self.select_room_label.hide()
        self.room_submit.hide()
        self.bookingnotfound_label.hide()
        self.roomnonotfound_label.hide()
        self.guestcheckedin_label.hide()
        self.guestalreadycheckedin_label.hide()

        if not hide:
            self.show()

        self.__clicked()

    def __clicked(self):
        self.booking_submit.clicked.connect(lambda: self.__book_sub())
        self.room_submit.clicked.connect(lambda: self.__room_sub())
    
    def __book_sub(self):
        self.select_roomno.hide()
        self.select_room_label.hide()
        self.room_submit.hide()
        self.bookingnotfound_label.hide()
        self.roomnonotfound_label.hide()
        self.guestalreadycheckedin_label.hide()
        self.guestcheckedin_label.hide()
         
        sql_exec = 'SELECT* FROM reservation_list WHERE booking_id = %s'
        sql_arg = (self.booking_Id.text())

        sql_connect.sql.cursor.execute(sql_exec, sql_arg)
        self.row = sql_connect.sql.cursor.fetchall()

        if len(self.row) == 0:
            self.bookingnotfound_label.show()
        else:
            sql_exec = 'SELECT EXISTS(SELECT* FROM guest_list WHERE guest_id = %s AND status = 1)'

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            checkin_present = sql_connect.sql.cursor.fetchone()

            if checkin_present[0] != 0:
                self.guestalreadycheckedin_label.show()
            else:
                self.select_room_label.show()
                self.select_roomno.show()
                self.room_submit.show()

                sql_exec = 'SELECT room_no FROM rooms_list WHERE room_type = %s AND status = 0'
                sql_arg = (self.row[0][7])
                
                sql_connect.sql.cursor.execute(sql_exec, sql_arg)
                room_no = sql_connect.sql.cursor.fetchall()

                for x in room_no:
                    self.select_roomno.addItem(str(x[0]))

    def __room_sub(self):
        self.roomnonotfound_label.hide()
        self.guestalreadycheckedin_label.hide()

        if self.select_roomno.currentIndex() == 0:
            self.roomnonotfound_label.show()
        else: 
            sql_exec = 'SELECT EXISTS(SELECT* FROM guest_list WHERE guest_id = %s AND status = 1)'
            sql_arg = (self.booking_Id.text())

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            checkin_present = sql_connect.sql.cursor.fetchone()

            if checkin_present[0] != 0:
                self.guestalreadycheckedin_label.show()           
            else:    
                sql_arg = []

                for value in range(6):
                    sql_arg.append(self.row[0][value])
                sql_arg.append(self.select_roomno.currentText())
                for value in range(8,10):
                    sql_arg.append(self.row[0][value])
                sql_arg.append(1)
                sql_arg[2] = sql_arg[2].strftime('%Y-%m-%d')
                sql_arg[7] = sql_arg[7].strftime('%Y-%m-%d')
                sql_arg[8] = sql_arg[8].strftime('%Y-%m-%d')

                sql_exec = 'INSERT INTO guest_list VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

                sql_connect.sql.cursor.execute(sql_exec, sql_arg)

                sql_exec = 'UPDATE rooms_list SET status = 1 WHERE room_no = %s'
                sql_arg = (self.select_roomno.currentText())

                sql_connect.sql.cursor.execute(sql_exec, sql_arg)
                sql_connect.sql.connect.commit()

                self.guestcheckedin_label.show()

    def clear(self):
        self.booking_Id.clear()
        self.select_roomno.hide()
        self.select_room_label.hide()
        self.room_submit.hide()
        self.bookingnotfound_label.hide()
        self.roomnonotfound_label.hide()
        self.guestalreadycheckedin_label.hide()
        self.guestcheckedin_label.hide()