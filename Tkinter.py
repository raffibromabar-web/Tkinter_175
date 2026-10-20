import tkinter as tk

#Warna
WARNA_BG = "#2e3480"        
WARNA_INPUT = "#374eff"     
WARNA_TEKS = "white"
WARNA_HASIL = "#E3F2FD"    

def hasil_prediksi():
    # Hasilnya TI
    popup = tk.Toplevel(root)
    popup.title("Hasil Prediksi")
    popup.geometry("420x150")
    popup.config(bg=WARNA_BG)

    label_hasil = tk.Label(
        popup,
        text="Prediksi Prodi: Teknologi Informasi",
        font=("Arial", 14, "bold"),
        bg=WARNA_BG,
        fg=WARNA_HASIL
    )
    label_hasil.pack(expand=True)


root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x680")
root.config(bg=WARNA_BG)

label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 18, "bold"),
    bg=WARNA_BG,
    fg=WARNA_TEKS
)
label_judul.pack(pady=20)

frame_input = tk.Frame(root, bg=WARNA_BG)
frame_input.pack()

list_entry = []
for i in range(10):
    label_nilai = tk.Label(
        frame_input,
        text="Nilai Mata Pelajaran " + str(i + 1) + ":",
        font=("Arial", 12),
        bg=WARNA_BG,
        fg=WARNA_TEKS
    )
    label_nilai.grid(row=i, column=0, sticky="e", padx=10, pady=4)

    entry_nilai = tk.Entry(
        frame_input,
        width=20,
        font=("Arial", 10, "bold"),
        bg=WARNA_INPUT,
        fg=WARNA_TEKS,
        insertbackground=WARNA_TEKS,
        relief="flat",
        bd=4
    )
    entry_nilai.grid(row=i, column=1, sticky="w", padx=10, pady=4)

    list_entry.append(entry_nilai)

label_jurusan = tk.Label(
    root,
    text="Pilihan Jurusan Anda:",
    font=("Arial", 12),
    bg=WARNA_BG,
    fg=WARNA_TEKS
)
label_jurusan.pack(pady=(20, 5))

pilihan_jurusan = tk.StringVar()
pilihan_jurusan.set("Teknologi Informasi")

dropdown_jurusan = tk.OptionMenu(
    root,
    pilihan_jurusan,
    "Teknologi Informasi",
    "Teknik Elektro",
    "Teknik Sipil",
    "Kedokteran",
    "Manajemen"
)