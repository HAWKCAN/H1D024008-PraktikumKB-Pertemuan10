import random
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# --- DATA BARANG (Dari Gambar Ketentuan) ---
# Format: (Nama, Keuntungan, Ukuran)
barang = [
    ("Barang1", 10, 5),
    ("Barang2", 40, 4),
    ("Barang3", 30, 6),
    ("Barang4", 50, 3),
    ("Barang5", 35, 7)
]

# --- FUNGSI FITNESS ---
def hitung_fitness(kromosom, barang, kapasitas):
    total_keuntungan = 0
    total_ukuran = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_keuntungan += barang[i][1]
            total_ukuran += barang[i][2]
    if total_ukuran > kapasitas:
        return 0 # Penalti jika melebihi kapasitas
    return total_keuntungan

# --- INISIALISASI POPULASI ---
def inisialisasi_populasi(jumlah_populasi, jumlah_gen):
    return [[random.randint(0, 1) for _ in range(jumlah_gen)] for _ in range(jumlah_populasi)]

# --- METODE SELEKSI (ROULETTE WHEEL) - NIM 08 ---
def roulette_wheel_selection(populasi, fitness_populasi):
    total_fitness = sum(fitness_populasi)
    if total_fitness == 0:
        idx = random.randrange(len(populasi))
        return populasi[idx], idx
    r = random.uniform(0, total_fitness)
    kumulatif = 0
    for i, fitness in enumerate(fitness_populasi):
        kumulatif += fitness
        if r <= kumulatif:
            return populasi[i], i
    return populasi[-1], len(populasi)-1

# --- METODE CROSSOVER (UNIFORM) - NIM 08 ---
def uniform_crossover(parent1, parent2):
    anak1, anak2 = [], []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            anak1.append(parent1[i])
            anak2.append(parent2[i])
        else:
            anak1.append(parent2[i])
            anak2.append(parent1[i])
    return anak1, anak2

# --- METODE MUTASI (UNIFORM) - NIM 08 ---
def uniform_mutation(kromosom, mutation_rate=0.1):
    kromosom = list(kromosom)
    for i in range(len(kromosom)):
        if random.random() < mutation_rate:
            kromosom[i] = 1 - kromosom[i]
    return kromosom

# --- FUNGSI UTAMA GA (Dipanggil oleh Tombol GUI) ---
def jalankan_ga():
    try:
        # Mengambil input kapasitas dari antarmuka Tkinter
        kapasitas_maksimal = int(entry_kapasitas.get())
        if kapasitas_maksimal <= 0:
            messagebox.showerror("Error Input", "Kapasitas tas harus lebih besar dari 0.")
            return
    except ValueError:
        messagebox.showerror("Error Input", "Masukkan kapasitas berupa angka bulat!")
        return

    # Parameter GA
    jumlah_generasi = 50
    jumlah_populasi = 20
    prob_crossover = 0.8
    prob_mutasi = 0.1
    jumlah_gen = len(barang)
    
    populasi = inisialisasi_populasi(jumlah_populasi, jumlah_gen)
    
    best_fitness_list = []
    best_individu_overall = None
    best_fitness_overall = -1

    for _ in range(jumlah_generasi):
        fitness_populasi = [hitung_fitness(ind, barang, kapasitas_maksimal) for ind in populasi]
        
        current_best_fitness = max(fitness_populasi)
        best_fitness_list.append(current_best_fitness)
        
        if current_best_fitness > best_fitness_overall:
            best_fitness_overall = current_best_fitness
            best_individu_overall = populasi[fitness_populasi.index(current_best_fitness)]

        new_populasi = []
        while len(new_populasi) < jumlah_populasi:
            
            # 1. Seleksi: ROULETTE WHEEL SELECTION
            p1, _ = roulette_wheel_selection(populasi, fitness_populasi)
            p2, _ = roulette_wheel_selection(populasi, fitness_populasi)

            # 2. Crossover: UNIFORM CROSSOVER
            if random.random() < prob_crossover:
                a1, a2 = uniform_crossover(p1, p2)
            else:
                a1, a2 = p1[:], p2[:]

            # 3. Mutasi: UNIFORM MUTATION
            if random.random() < prob_mutasi: a1 = uniform_mutation(a1)
            if random.random() < prob_mutasi: a2 = uniform_mutation(a2)

            new_populasi.extend([a1, a2])

        populasi = new_populasi[:jumlah_populasi]

    # --- MENAMPILKAN HASIL KE TEXTBOX GUI ---
    selected_items = [barang[i][0] for i in range(len(best_individu_overall)) if best_individu_overall[i] == 1]
    total_profit = hitung_fitness(best_individu_overall, barang, kapasitas_maksimal)
    total_size = sum([barang[i][2] for i in range(len(best_individu_overall)) if best_individu_overall[i] == 1])
    
    hasil_teks = f"=== HASIL OPTIMASI KNAPSACK (NIM **08) ===\n"
    hasil_teks += f"Kapasitas Maksimal Tas: {kapasitas_maksimal}\n\n"
    hasil_teks += f"Kromosom Terbaik: {best_individu_overall}\n"
    hasil_teks += f"Total Keuntungan: {total_profit}\n"
    hasil_teks += f"Total Ukuran (Bobot): {total_size}\n\n"
    hasil_teks += "Barang yang Terpilih:\n"
    for item in selected_items:
        hasil_teks += f" - {item}\n"
        
    # Kosongkan text box lalu masukkan hasil terbaru
    text_hasil.delete(1.0, tk.END)
    text_hasil.insert(tk.END, hasil_teks)

    # Menampilkan Grafik Matplotlib
    plt.figure(figsize=(7, 5))
    plt.plot(range(1, jumlah_generasi+1), best_fitness_list, color='blue', linewidth=2)
    plt.title(f'Perkembangan Keuntungan per Generasi\n(Kapasitas: {kapasitas_maksimal})')
    plt.xlabel('Generasi')
    plt.ylabel('Keuntungan Maksimal')
    plt.grid(True)
    plt.show()

# ==========================================
# --- KONFIGURASI GUI TKINTER ---
# ==========================================
jendela = tk.Tk()
jendela.title("Optimasi Knapsack - Algoritma Genetika")
jendela.geometry("450x450")
jendela.configure(bg="#f0f0f0")

# Label Judul
label_judul = tk.Label(jendela, text="Knapsack Problem (NIM: **08)", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
label_judul.pack(pady=10)

# Frame untuk Input
frame_input = tk.Frame(jendela, bg="#f0f0f0")
frame_input.pack(pady=10)

label_kapasitas = tk.Label(frame_input, text="Masukkan Kapasitas Tas:", font=("Helvetica", 10), bg="#f0f0f0")
label_kapasitas.grid(row=0, column=0, padx=5)

entry_kapasitas = tk.Entry(frame_input, width=10, font=("Helvetica", 12), justify="center")
entry_kapasitas.grid(row=0, column=1, padx=5)

# Tombol Eksekusi
btn_jalankan = tk.Button(jendela, text="Jalankan Algoritma Genetika", command=jalankan_ga, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white", cursor="hand2")
btn_jalankan.pack(pady=10)

# Kotak Teks untuk Menampilkan Hasil
label_hasil = tk.Label(jendela, text="Hasil Solusi Terbaik:", font=("Helvetica", 10, "bold"), bg="#f0f0f0")
label_hasil.pack(anchor="w", padx=20)

text_hasil = tk.Text(jendela, height=12, width=50, font=("Consolas", 10))
text_hasil.pack(padx=20, pady=5)

# Jalankan Aplikasi GUI
if __name__ == "__main__":
    jendela.mainloop()