import sql_connect
from PyQt5.QtWidgets import QMainWindow
from addroom_list_ui import Ui_addroomlist

class addroom_list(QMainWindow, Ui_addroomlist):
    def __init__(self, hide):
        super().__init__()

        self.roomadded_label.hide()
        self.roompresent_label.hide()

        if not hide:
            self.show()
        
        self.__showroomtype()
        self.__clicked()

    def __clicked(self):
        self.submit.clicked.connect(lambda: self.__addroom_list())

    def __showroomtype(self):
        self.roomtype.clear()
        self.roomtype.addItem('Room Type')
        self.roomtype.setCurrentIndex(0)

        sql_exec = 'SELECT room_type FROM room_type'

        sql_connect.sql.cursor.execute(sql_exec)
        room_type = sql_connect.sql.cursor.fetchall()

        for type in room_type:
            self.roomtype.addItem(str(type[0]))

    def __addroom_list(self):
            self.roomadded_label.hide()
            self.roompresent_label.hide()

            sql_exec = 'SELECT* FROM rooms_list WHERE room_no = %s'
            sql_arg = (self.roomno.text())

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            row = sql_connect.sql.cursor.fetchall()
            
            if len(row) == 0:
                sql_exec = 'INSERT INTO rooms_list VALUES (%s, %s, %s)'
                sql_arg = (self.roomno.text(), self.roomtype.currentText(), 0)

                sql_connect.sql.cursor.execute(sql_exec, sql_arg)

                sql_exec = 'UPDATE room_type SET total_rooms = total_rooms + 1 WHERE room_type = %s'
                sql_arg = (self.roomtype.currentText())

                sql_connect.sql.cursor.execute(sql_exec, sql_arg)
                sql_connect.sql.connect.commit()

                self.roomadded_label.show()
                self.__showroomtype()
            else:
                self.roompresent_label.show()

    def clear(self):
        self.roomno.clear()
        self.roomadded_label.hide()
        self.roompresent_label.hide()
        self.__showroomtype()

    def refresh(self):
        self.__showroomtype()