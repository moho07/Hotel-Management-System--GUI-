import pymysql

class Mysqlconnect():

    def __del__(self):
        self.connect.close()
    
    def __init__(self):
        self.connect()

    def connect(self):
        self.connect = pymysql.connect(
            host = 'localhost',
            port = 3307,
            user = 'root', 
            password = 'root', 
            db = 'hotelmanagement'
        )

        self.cursor = self.connect.cursor()

global sql

sql = Mysqlconnect()