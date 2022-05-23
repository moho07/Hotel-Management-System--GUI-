import sql_connect
from PyQt5.QtWidgets import QMainWindow
from addroom_type_ui import Ui_addroomtype

class addroom_type(QMainWindow, Ui_addroomtype):
    def __init__(self, hide):
        super().__init__()

        self.roomtypeadded_label.hide()
        self.roomtypepresent_label.hide()

        if not hide:
            self.show()
        
        self.__clicked()

    def __clicked(self):
        self.submit.clicked.connect(lambda: self.__addroom_type())

    def __addroom_type(self):
            self.roomtypeadded_label.hide()
            self.roomtypepresent_label.hide()

            sql_exec = 'SELECT* FROM room_type WHERE room_type = %s'
            sql_arg = (self.roomtype.text())

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            row = sql_connect.sql.cursor.fetchall()

            if len(row) == 0:
                sql_exec = 'INSERT INTO room_type VALUES (%s, %s, %s)'
                sql_arg = (self.roomtype.text(), self.maxguests.text(), 0)

                sql_connect.sql.cursor.execute(sql_exec, sql_arg)
                sql_connect.sql.connect.commit()

                self.roomtypeadded_label.show()
            else:
                self.roomtypepresent_label.show()

    def clear(self):
        self.roomtype.clear()
        self.maxguests.clear()
        self.roomtypeadded_label.hide()
        self.roomtypepresent_label.hide()

    def refresh(self):
        pass
