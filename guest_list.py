import sql_connect
import PyQt5.QtWidgets 
from PyQt5.QtWidgets import QMainWindow
from guest_list_ui import Ui_guest_list

class guest_list(QMainWindow, Ui_guest_list):
    def __init__(self, hide):
        super().__init__()

        self.resultsnotfound_label.hide()

        if not hide:
            self.show()

        self.__clicked()
    
    def __clicked(self):
        self.submit.clicked.connect(lambda: self.__infosubmit())
        self.showall.clicked.connect(lambda: self.__showall())

    def __infosubmit(self):
        self.guest_view.setRowCount(0)
        self.resultsnotfound_label.hide()

        guest_name = self.guestname.text()

        sql_exec = "SELECT* FROM guest_list WHERE guest_name LIKE CONCAT('%%', %s, '%%')"
        sql_arg = (guest_name)

        sql_connect.sql.cursor.execute(sql_exec, sql_arg)
        row = sql_connect.sql.cursor.fetchall()

        if len(row) == 0:
            self.resultsnotfound_label.show()
        else:
            for row_value in row:
                rowPosition = self.guest_view.rowCount()
                self.guest_view.insertRow(rowPosition)

                row_value = list(row_value)
                row_value[2] = row_value[2].strftime('%Y-%m-%d')
                row_value[6] = str(row_value[6])
                row_value[7] = row_value[7].strftime('%Y-%m-%d')
                row_value[8] = row_value[8].strftime('%Y-%m-%d')
                if int.from_bytes(row_value[9], "big") == 1:
                    row_value[9] = 'Checked In'
                else:
                    row_value[9] = 'Checked Out'
                row_value = tuple(row_value)

                for col_no,col in enumerate(row_value):
                    self.guest_view.setItem(rowPosition, col_no, PyQt5.QtWidgets.QTableWidgetItem(col))
    
    def __showall(self):
        self.guest_view.setRowCount(0)
        self.resultsnotfound_label.hide()

        sql_exec = 'SELECT* FROM guest_list'

        sql_connect.sql.cursor.execute(sql_exec)
        row = sql_connect.sql.cursor.fetchall()

        if len(row) == 0:
            self.resultsnotfound_label.show()
        else:
            for row_value in row:
                rowPosition = self.guest_view.rowCount()
                self.guest_view.insertRow(rowPosition)

                row_value = list(row_value)
                row_value[2] = row_value[2].strftime('%Y-%m-%d')
                row_value[6] = str(row_value[6])
                row_value[7] = row_value[7].strftime('%Y-%m-%d')
                row_value[8] = row_value[8].strftime('%Y-%m-%d')
                if int.from_bytes(row_value[9], "big") == 1:
                    row_value[9] = 'Checked In'
                else:
                    row_value[9] = 'Checked Out'
                row_value = tuple(row_value)

                for col_no,col in enumerate(row_value):
                    self.guest_view.setItem(rowPosition, col_no, PyQt5.QtWidgets.QTableWidgetItem(col))

    def clear(self):
        self.guestname.clear()
        self.guest_view.setRowCount(0)
        self.resultsnotfound_label.hide()
