import sql_connect
from PyQt5.QtWidgets import QMainWindow
from removeroom_list_ui import Ui_removeroom

class removeroom_list(QMainWindow, Ui_removeroom):
    def __init__(self, hide):
        super().__init__()

        self.pleaseselectroomno_label.hide()
        self.roomisoccupied_label.hide()
        self.roomremoved_label.hide()

        if not hide:
            self.show()
        
        self.__showroomlist()
        self.__clicked()

    def __clicked(self):
        self.submit.clicked.connect(lambda: self.__removeroom_list())

    def __showroomlist(self):
        self.roomno.clear()
        self.roomno.addItem('Room Number')
        self.roomno.setCurrentIndex(0)

        sql_exec = 'SELECT room_no FROM rooms_list'

        sql_connect.sql.cursor.execute(sql_exec)
        room_no = sql_connect.sql.cursor.fetchall()

        for no in room_no:
            self.roomno.addItem(str(no[0]))

    def __removeroom_list(self):
        self.pleaseselectroomno_label.hide()
        self.roomisoccupied_label.hide()
        self.roomremoved_label.hide()

        if self.roomno.currentIndex == 0:
            self.pleaseselectroomno_label.show()
        else:
            sql_exec = 'SELECT EXISTS(SELECT* FROM guest_list WHERE room_no = %s AND status = 1)'
            sql_arg = (self.roomno.currentIndex())

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            room_occupied = sql_connect.sql.cursor.fetchone()

            if room_occupied[0] != 0:
                self.roomisoccupied_label.show()
            else:

                sql_exec = '''UPDATE room_type SET total_rooms = total_rooms - 1 WHERE room_type IN 
                           (SELECT room_type FROM rooms_list WHERE room_no = %s)'''
                            
                sql_connect.sql.cursor.execute(sql_exec, sql_arg)

                sql_exec = 'DELETE FROM rooms_list WHERE room_no = %s'
                
                sql_connect.sql.cursor.execute(sql_exec, sql_arg)
                sql_connect.sql.connect.commit()

                self.roomremoved_label.show()
                self.__showroomlist()


    def clear(self):
        self.roomno.setCurrentIndex(0)
        self.pleaseselectroomno_label.hide()
        self.roomisoccupied_label.hide()
        self.roomremoved_label.hide()

    def refresh(self):
        self.__showroomlist()
    
    
