from models.anggota_model import AnggotaModel

model = AnggotaModel()

# 1. Menguji fungsi Create (menambah anggota baru, dilewati jika sudah ada)
nama_baru = "Budi Santoso"
alamat_baru = "Jl. Merdeka No. 10"
nama_tersimpan = [a['nama'] for a in model.get_all_anggota()]

print("Menambahkan data anggota...")
if nama_baru in nama_tersimpan:
    print(f"Dilewati, anggota '{nama_baru}' sudah ada.")
else:
    model.create_anggota(nama_baru, alamat_baru)
    print("Data anggota berhasil disimpan!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Anggota ===")
for anggota in model.get_all_anggota():
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")