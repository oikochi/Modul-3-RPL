import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding semua tombol
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout)

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan/update/hapus
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")
            self.view.btn_update.configure(state="disabled")
            self.view.btn_hapus.configure(state="disabled")

        self.muat_data_tabel()

    def logout(self):
        self.view.destroy()
        from controllers.auth_controller import AuthController  # import lokal, hindari circular import
        app_login = AuthController()
        app_login.run()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        data_buku = self.model.get_all_buku()
        for no, buku in enumerate(data_buku, start=1):
            self.view.tabel.insert(
                "", "end",
                iid=str(buku['id_buku']),   # id asli disimpan sebagai iid (tersembunyi dari tampilan)
                values=(no, buku['judul'], buku['penulis'], buku['tahun_terbit'])
            )

    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.kosongkan_input()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def update_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

        id_buku = self.view.id_terpilih()
        if id_buku is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris buku yang mau diperbarui!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.view.kosongkan_input()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        id_buku = self.view.id_terpilih()
        if id_buku is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris buku yang mau dihapus!")
            return

        if not messagebox.askyesno("Konfirmasi", "Yakin mau menghapus data ini?"):
            return

        try:
            if self.model.delete_buku(id_buku):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.muat_data_tabel()
        except Exception as e:
            messagebox.showerror(
                "Gagal Menghapus",
                f"Buku ini tidak bisa dihapus.\nKemungkinan masih terkait data peminjaman.\n\nDetail: {e}"
            )

    def run(self):
        self.view.mainloop()