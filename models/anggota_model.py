from config.database import Database


class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def _execute(self, query, val):
        if not self.conn:
            return False
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

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name} ORDER BY id_anggota"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_anggota(self, nama, alamat):
        query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
        return self._execute(query, (nama, alamat))

    def update_anggota(self, id_anggota, nama, alamat):
        query = f"UPDATE {self.table_name} SET nama=%s, alamat=%s WHERE id_anggota=%s"
        return self._execute(query, (nama, alamat, id_anggota))

    def delete_anggota(self, id_anggota):
        query = f"DELETE FROM {self.table_name} WHERE id_anggota=%s"
        return self._execute(query, (id_anggota,))