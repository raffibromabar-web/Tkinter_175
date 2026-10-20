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
    