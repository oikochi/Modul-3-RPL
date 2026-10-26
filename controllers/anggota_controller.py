from tkinter import messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.view.btn_simpan.configure(command=self.simpan)
        self.view.btn_update.configure(command=self.perbarui)
        self.view.btn_hapus.configure(command=self.hapus)

        self.muat_data()

    def muat_data(self):
        self.view.isi_tabel(self.model.get_all_anggota())

    def _validasi(self, nama, alamat):
        if not nama.strip() or not alamat.strip():
            messagebox.showwarning("Peringatan", "Nama dan alamat wajib diisi!")
            return False
        return True

    def simpan(self):
        nama, alamat = self.view.ambil_input()
        if not self._validasi(nama, alamat):
            return
        try:
            self.model.create_anggota(nama.strip(), alamat.strip())
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan.")
            self.view.kosongkan_input()
            self.muat_data()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyimpan data: {e}")

    def perbarui(self):
        id_anggota = self.view.id_terpilih()
        if id_anggota is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris yang mau diperbarui!")
            return
        nama, alamat = self.view.ambil_input()
        if not self._validasi(nama, alamat):
            return
        try:
            self.model.update_anggota(id_anggota, nama.strip(), alamat.strip())
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui.")
            self.view.kosongkan_input()
            self.muat_data()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memperbarui data: {e}")

    def hapus(self):
        id_anggota = self.view.id_terpilih()
        if id_anggota is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris yang mau dihapus!")
            return
        if not messagebox.askyesno("Konfirmasi", "Yakin mau menghapus data ini?"):
            return
        try:
            self.model.delete_anggota(id_anggota)
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus.")
            self.view.kosongkan_input()
            self.muat_data()
        except Exception:
            messagebox.showerror(
                "Error",
                "Data tidak bisa dihapus. Kemungkinan anggota ini masih tercatat di data peminjaman."
            )

    def jalankan(self):
        self.view.mainloop()