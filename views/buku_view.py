import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("800x450")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1)  # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=2)  # Kolom Kanan (Tabel lebih lebar)
        self.grid_rowconfigure(0, weight=1)

        # -----------------------------------------
        # FRAME KIRI: FORMULIR INPUT BUKU
        # -----------------------------------------
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold")).pack(pady=15)

        self.entry_judul = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Judul Buku")
        self.entry_judul.pack(pady=10, padx=15, fill="x")

        self.entry_penulis = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Penulis")
        self.entry_penulis.pack(pady=10, padx=15, fill="x")

        self.entry_tahun = ctk.CTkEntry(self.frame_kiri, placeholder_text="Tahun Terbit (Misal: 2024)")
        self.entry_tahun.pack(pady=10, padx=15, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=20, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue")
        self.btn_update.pack(pady=10, padx=15, fill="x")

        self.btn_hapus = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red")
        self.btn_hapus.pack(pady=10, padx=15, fill="x")

        # -----------------------------------------
        # FRAME KANAN: TABEL DAFTAR BUKU
        # -----------------------------------------
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Koleksi Buku", font=("Arial", 16, "bold")).pack(pady=15)

        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("judul", width=150)
        self.tabel.column("penulis", width=120)
        self.tabel.column("tahun", width=80, anchor="center")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

        # Saat baris tabel diklik, form terisi data baris tersebut
        self.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_pilihan)

    # ---------- Method bantu (hanya urusan tampilan, tanpa SQL) ----------
    def ambil_input(self):
        return self.entry_judul.get(), self.entry_penulis.get(), self.entry_tahun.get()

    def kosongkan_input(self):
        self.entry_judul.delete(0, "end")
        self.entry_penulis.delete(0, "end")
        self.entry_tahun.delete(0, "end")

    def isi_tabel(self, data):
        for baris in self.tabel.get_children():
            self.tabel.delete(baris)
        for b in data:
            self.tabel.insert("", "end",
                              values=(b["id_buku"], b["judul"], b["penulis"], b["tahun_terbit"]))

    def id_terpilih(self):
        pilihan = self.tabel.selection()
        if not pilihan:
            return None
        return self.tabel.item(pilihan[0])["values"][0]

    def isi_form_dari_pilihan(self, event=None):
        pilihan = self.tabel.selection()
        if not pilihan:
            return
        _, judul, penulis, tahun = self.tabel.item(pilihan[0])["values"]
        self.kosongkan_input()
        self.entry_judul.insert(0, judul)
        self.entry_penulis.insert(0, penulis)
        self.entry_tahun.insert(0, tahun)


# Blok eksekusi untuk menguji tampilan grafis
if __name__ == "__main__":
    app = BukuView()
    app.mainloop()