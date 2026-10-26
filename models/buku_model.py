from config.database import Database


class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def _execute(self, query, val):
        if not self.conn:
            raise ConnectionError("Tidak terhubung ke database. Pastikan MySQL di Laragon sudah Start.")
        cursor = self.conn.cursor()
        try:
            cursor.execute(query, val)
            self.conn.commit()
            return True
        except Exception:
            self.conn.rollback()
            raise
        finally:
            cursor.close()

    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name} ORDER BY id_buku"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        query = f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
        return self._execute(query, (judul, penulis, tahun_terbit))

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        query = f"UPDATE {self.table_name} SET judul=%s, penulis=%s, tahun_terbit=%s WHERE id_buku=%s"
        return self._execute(query, (judul, penulis, tahun_terbit, id_buku))

    def delete_buku(self, id_buku):
        query = f"DELETE FROM {self.table_name} WHERE id_buku=%s"
        return self._execute(query, (id_buku,))