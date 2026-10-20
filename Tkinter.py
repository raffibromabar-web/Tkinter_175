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