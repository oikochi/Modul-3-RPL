import customtkinter as ctk
from tkinter import ttk


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Anggota")
        self.geometry("800x450")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # -----------------------------------------
        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        # -----------------------------------------
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold")).pack(pady=15)

        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota")
        self.entry_nama.pack(pady=10, padx=15, fill="x")

        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat")
        self.entry_alamat.pack(pady=10, padx=15, fill="x")

        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=20, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue")
        self.btn_update.pack(pady=10, padx=15, fill="x")

        self.btn_hapus = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red")
        self.btn_hapus.pack(pady=10, padx=15, fill="x")

        # -----------------------------------------
        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        # -----------------------------------------
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold")).pack(pady=15)

        kolom = ("id", "nama", "alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        self.tabel.heading("id", text="ID")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        self.tabel.column("id", width=40, anchor="center")
        self.tabel.column("nama", width=150)
        self.tabel.column("alamat", width=200)

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

        self.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_pilihan)

    # ---------- Method bantu ----------
    def ambil_input(self):
        return self.entry_nama.get(), self.entry_alamat.get()

    def kosongkan_input(self):
        self.entry_nama.delete(0, "end")
        self.entry_alamat.delete(0, "end")

    def isi_tabel(self, data):
        for baris in self.tabel.get_children():
            self.tabel.delete(baris)
        for a in data:
            self.tabel.insert("", "end", values=(a["id_anggota"], a["nama"], a["alamat"]))

    def id_terpilih(self):
        pilihan = self.tabel.selection()
        if not pilihan:
            return None
        return self.tabel.item(pilihan[0])["values"][0]

    def isi_form_dari_pilihan(self, event=None):
        pilihan = self.tabel.selection()
        if not pilihan:
            return
        _, nama, alamat = self.tabel.item(pilihan[0])["values"]
        self.kosongkan_input()
        self.entry_nama.insert(0, nama)
        self.entry_alamat.insert(0, alamat)


if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()