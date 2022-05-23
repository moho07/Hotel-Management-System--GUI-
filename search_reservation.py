import PyQt5.QtWidgets 
import sql_connect
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate
from search_reservation_ui import Ui_search_reservation

class search_reserve(QMainWindow, Ui_search_reservation):
    def __init__(self, hide):
        super().__init__()

        self.resultsnotfound_label.hide()

        if not hide:
            self.show()

        self.__clicked()
    
    def __clicked(self):
        self.submit.clicked.connect(lambda: self.__infosubmit())

    def __infosubmit(self):
        self.search_view.setRowCount(0)
        self.resultsnotfound_label.hide()

        from_date = self.from_date.date().toString('yyyy-MM-dd')
        to_date = self.to_date.date().toString('yyyy-MM-dd')

        sql_exec = 'SELECT* FROM reservation_list WHERE date(checkin) BETWEEN %s AND %s'
        sql_arg = (from_date, to_date)

        sql_connect.sql.cursor.execute(sql_exec, sql_arg)
        row = sql_connect.sql.cursor.fetchall()

        if len(row) == 0:
            self.resultsnotfound_label.show()
        else:
            for row_value in row:
                rowPosition = self.search_view.rowCount()
                self.search_view.insertRow(rowPosition)

                row_value = list(row_value)
                row_value[2] = row_value[2].strftime('%Y-%m-%d')
                row_value[6] = str(row_value[6])
                row_value[8] = row_value[8].strftime('%Y-%m-%d')
                row_value[9] = row_value[9].strftime('%Y-%m-%d')
                row_value[10] = row_value[10].strftime('%Y-%m-%d')
                row_value = tuple(row_value)

                for col_no,col in enumerate(row_value):
                    self.search_view.setItem(rowPosition, col_no, PyQt5.QtWidgets.QTableWidgetItem(col))

    def clear(self):
        date = QDate(2000,1,1)
        self.search_view.setRowCount(0)
        self.resultsnotfound_label.hide()
        self.from_date.setDate(date)
        self.to_date.setDate(date)