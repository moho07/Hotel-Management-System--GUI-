import random
import string
import time
import re
import windows
import sql_connect

from PyQt5.QtWidgets import (QMainWindow, QDesktopWidget)
from PyQt5.QtCore import QDate
from showbookingid import showbookingid
from make_reservation_ui import Ui_make_reservation

class make_reserve(QMainWindow, Ui_make_reservation):
    def __init__(self, hide):
        super().__init__()

        self.center()

        self.infoinvalid_label.hide()

        if not hide:
            self.show()

        self.__signal()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def __signal(self):
        self.submit.clicked.connect(lambda: self.__infosubmit())
        self.guests.currentIndexChanged.connect(lambda: self.set_room_type())
        self.checkin.dateTimeChanged.connect(lambda: self.set_room_type())
        self.checkout.dateTimeChanged.connect(lambda: self.set_room_type())

    def set_room_type(self):
        current_people = self.guests.currentIndex()
        self.checkin_date = self.checkin.date().toString('yyyy-MM-dd')

        self.roomtype.clear()
        self.roomtype.addItem('Room Type')
        self.roomtype.setCurrentIndex(0)

        if current_people != 0:
            sql_exec = '''SELECT room_type FROM room_type WHERE max_people >= %s 
            AND total_rooms > (SELECT COUNT(room_type) FROM reservation_list WHERE %s BETWEEN checkin AND checkout)'''
            sql_arg = (current_people, self.checkin_date)

            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            rooms_available = sql_connect.sql.cursor.fetchall()
            
            for x in rooms_available:
                self.roomtype.addItem(x[0])

    def __infosubmit(self):
        self.infoinvalid_label.hide()

        fullname_text = self.fname.text() + ' ' + self.mname.text() + ' ' + self.lname.text()
        birthday_date = self.birthday.date().toString('yyyy-MM-dd')
        address_text = self.buildingno.text() + ',' + self.locality.text() + ',' + self.street.text() + ',' + self.city.text() + ',' + self.state.currentText() + ',' + self.pincode.text()
        self.checkin_date = self.checkin.date().toString('yyyy-MM-dd')
        self.checkout_date = self.checkout.date().toString('yyyy-MM-dd')
        self.current_date = QDate.currentDate().toString('yyyy-MM-dd')
        self.booking_id = self.__get_bookingid()

        if not self.__infocheck():
            self.infoinvalid_label.show()
        else:
            sql_exec = 'INSERT INTO reservation_list VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            sql_arg = (self.booking_id, fullname_text, birthday_date, self.phone.text(), self.email.text(), address_text, 
            self.guests.currentText(), self.roomtype.currentText(), self.checkin_date, self.checkout_date, self.current_date)
            
            sql_connect.sql.cursor.execute(sql_exec, sql_arg)
            sql_connect.sql.connect.commit()

            self.hide()
            self.show_bookingid_window = showbookingid(self.booking_id)

            self.show_bookingid_window.ok.clicked.connect(lambda: self.__openwindow())
            self.show_bookingid_window.checkin.clicked.connect(lambda: self.__checkin())
        
    def __infocheck(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        checkin_d = time.strptime(self.checkin_date, "%Y-%m-%d")
        checkout_d = time.strptime(self.checkout_date, "%Y-%m-%d")
        current_d = time.strptime(self.current_date, "%Y-%m-%d")

        if (not self.fname.text().isalpha() or not self.lname.text().isalpha() or not self.mname.text().isalpha() or not self.phone.text().isnumeric()
        or len(self.phone.text()) != 10 or not re.fullmatch(regex, self.email.text()) or self.buildingno.text() == '' or not self.locality.text().isalpha() or not self.street.text().isalpha() 
        or not self.city.text().isalpha() or self.state.currentIndex() == 0 or not self.pincode.text().isnumeric() or self.guests.currentIndex() == 0 or checkin_d >= checkout_d 
        or checkin_d < current_d):
            return False

        return True

    def __openwindow(self):
        self.show_bookingid_window.close()
        self.clear()
        self.show()

    def __checkin(self):
        self.show_bookingid_window.close()
        windows.checkin_window.show()
        windows.checkin_window.booking_Id.setText(self.booking_id)

    def __get_bookingid(self):
        letters = ''.join((random.choice(string.ascii_letters) for i in range(4)))
        digits = ''.join((random.choice(string.digits) for i in range(2)))

        sample_list = list(letters + digits)
        random.shuffle(sample_list)
        final_string = ''.join(sample_list)

        return final_string

    def clear(self):
        self.infoinvalid_label.hide()
        date = QDate(2000,1,1)
        self.fname.clear()
        self.mname.clear()
        self.lname.clear()
        self.birthday.setDate(date)
        self.gender.setCurrentIndex(0)
        self.phone.clear()
        self.email.clear()
        self.buildingno.clear()
        self.locality.clear()
        self.street.clear()
        self.city.clear()
        self.state.setCurrentIndex(0)
        self.pincode.clear()
        self.guests.setCurrentIndex(0)
        self.roomtype.setCurrentIndex(0)
        self.checkin.setDate(date)
        self.checkout.setDate(date)
        