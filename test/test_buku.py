from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Membuat objek model tanpa menjalankan koneksi database asli
    model = BukuModel.__new__(BukuModel)
    model.table_name = "buku"  # sesuaikan dengan __init__ BukuModel

    # Membuat mock untuk koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menjalankan fungsi create_buku
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memastikan query INSERT dieksekusi dengan parameter yang benar
    mock_cursor.execute.assert_called_once_with(
        f"INSERT INTO {model.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)",
        ("Buku Testing", "Penulis QA", 2026)
    )

    # Memastikan transaksi disimpan
    model.conn.commit.assert_called_once()

    # Memastikan cursor ditutup
    mock_cursor.close.assert_called_once()