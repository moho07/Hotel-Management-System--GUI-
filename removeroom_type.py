import sql_connect
from PyQt5.QtWidgets import QMainWindow
from removeroom_type_ui import Ui_removeroomtype

class removeroom_type(QMainWindow, Ui_removeroomtype):
    def __init__(self, hide):
        super().__init__()

        self.pleaseselectroomtype_label.hide()
        self.roomtypeisoccupied_label.hide()       
        self.roomtyperemoved_label.hide()

        if not hide:
            self.show()

        self.__showroomtype()
        self.__clicked()

    def __clicked(self):
        self.submit.clicked.connect(lambda: self.__removeroom_type())

    def __showroomtype(self):
        self.roomtype.clear()
        self.roomtype.addItem('Room Type')
        self.roomtype.setCurrentIndex(0)

        sql_exec = 'SELECT room_type FROM room_type'

        sql_connect.sql.cursor.execute(sql_exec)
        room_type = sql_connect.sql.cursor.fetchall()

        for type in room_type:
            self.roomtype.addItem(str(type[0]))

    def __removeroom_type(self):
        self.pleaseselectroomtype_label.hide()
        self.roomtypeisoccupied_label.hide()
        self.roomtyperemoved_label.hide()
        
        if self.roomtype.currentIndex == 0:
            self.pleaseselectroomtype_label.show()
        else:
            sql_exec = 'SELECT EXISTS(SELECT occupied_rooms FROM room_type WHERE room_type = %s)'
            sql_arg = (self.roomtype.currentIndex())

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            room_type_occupied = sql_connect.sql.cursor.fetchone()
            
            if room_type_occupied[0] != 0:
                self.roomtypeisoccupied_label.show()
            else:
                sql_exec = 'DELETE FROM room_type where room_type = %s'
                sql_arg = (self.roomtype.currentText())

                sql_connect.sql.cursor.execute(sql_exec, sql_arg)

                sql_exec = 'DELETE FROM rooms_list where room_type = %s'

                sql_connect.sql.cursor.execute(sql_exec, sql_arg)
                sql_connect.sql.connect.commit()

                self.roomtyperemoved_label.show()
                self.__showroomtype()
    
    def clear(self):
        self.roomtype.setCurrentIndex(0)
        self.pleaseselectroomtype_label.hide()
        self.roomtypeisoccupied_label.hide()
        self.roomtyperemoved_label.hide()

    def refresh(self):
        self.__showroomtype()