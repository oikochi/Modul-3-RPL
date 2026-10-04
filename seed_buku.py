from models.buku_model import BukuModel

model = BukuModel()

# 1. Hapus data dobel (sisakan 1 buku untuk tiap judul + penulis yang sama)
print("=== Membersihkan data dobel ===")
sudah_ada = set()
jumlah_dihapus = 0
for buku in sorted(model.get_all_buku(), key=lambda b: b['id_buku']):
    kunci = (buku['judul'], buku['penulis'])
    if kunci in sudah_ada:
        model.delete_buku(buku['id_buku'])
        print(f"Dihapus : [{buku['id_buku']}] {buku['judul']}")
        jumlah_dihapus += 1
    else:
        sudah_ada.add(kunci)
if jumlah_dihapus == 0:
    print("Tidak ada data dobel.")

# 2. Tambah buku bertema Genshin Impact (dilewati jika judulnya sudah ada)
print("\n=== Menambahkan buku Genshin ===")
buku_genshin = [
    ("A Traveler's Guide to Teyvat", "Paimon", 2020),
    ("Chronicles of Inazuma", "Kamisato Ayaka", 2021),
    ("Sumeru: The Akademiya Archives", "Alhaitham", 2022),
    ("Natlan: Land of Pyro", "Mavuika", 2024),
    ("The Art of Alchemy", "Albedo", 2020),
    ("Cooking in Teyvat", "Xiangling", 2021),
]
judul_tersimpan = {b['judul'] for b in model.get_all_buku()}
for judul, penulis, tahun in buku_genshin:
    if judul in judul_tersimpan:
        print(f"Dilewati (sudah ada): {judul}")
    else:
        model.create_buku(judul, penulis, tahun)
        print(f"Ditambahkan: {judul}")

# 3. Tampilkan hasil akhir
print("\n=== Daftar Buku Sekarang ===")
for buku in model.get_all_buku():
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")