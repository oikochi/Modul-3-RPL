import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = "localhost"
        self.db_name = "perpustakaan"
        self.username = "root"
        self.password = ""
        self.conn = None
        self.last_error = None

    def get_connection(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.db_name,
                user=self.username,
                password=self.password,
                use_pure=True   # <-- paksa pakai implementasi Python murni, hindari bug plugin DLL
            )
            if self.conn.is_connected():
                return self.conn
        except Error as e:
            self.last_error = str(e)
            print(f"Koneksi Gagal: {e}")
            return None