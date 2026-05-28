# Eksperimen Algoritma Genetika - Knapsack Problem (GUI)

**Nama** : FARIZ RAHMAN SYAHIDA
**NIM** : H1D024008
**Shift Awal** : C
**Shift Akhir** : G

---

## Deskripsi Program

Aplikasi Python ini menyelesaikan **0/1 Knapsack Problem** menggunakan Algoritma Genetika. Program sudah dilengkapi antarmuka _Graphical User Interface_ (GUI) menggunakan `Tkinter` agar pengguna bisa langsung memasukkan kapasitas tas dan melihat hasil optimasi beserta grafiknya.

## Penjelasan Logika & Metode (NIM: \*\*08)

### 1. Logika Algoritma Genetika

- **Kromosom & Fitness:** Solusi berupa biner (1 = barang dibawa, 0 = ditinggal). Nilai _fitness_ adalah total keuntungan. Jika bobot barang melebihi kapasitas tas, _fitness_ di-set menjadi 0 (penalti).
- **Seleksi (`Roulette Wheel`):** Induk dipilih secara acak, di mana individu dengan _fitness_ (keuntungan) tinggi memiliki peluang lebih besar untuk terpilih.
- **Crossover (`Uniform`):** Persilangan gen antar dua induk di mana setiap barang (gen) memiliki peluang 50:50 untuk diwariskan kepada anak.
- **Mutasi (`Uniform`):** Setiap gen pada anak memiliki peluang 10% untuk dibalik nilainya (0 menjadi 1, atau sebaliknya) agar menghasilkan variasi solusi.

### 2. Logika GUI (Tkinter)

- **Input (`Entry`):** Kotak teks untuk menangkap input angka batas kapasitas tas dari pengguna.
- **Eksekusi (`Button`):** Tombol yang ketika diklik akan memicu fungsi untuk menjalankan evolusi Algoritma Genetika sebanyak 50 generasi.
- **Output (`Text Box`):** Area teks yang secara otomatis diperbarui untuk menampilkan susunan kromosom terbaik, total untung, bobot, dan nama barang yang terpilih.
- **Visualisasi (`Matplotlib`):** Setelah evolusi selesai, program memanggil grafik untuk memvisualisasikan tren peningkatan _fitness_ (keuntungan) dari generasi ke generasi pada _window_ terpisah.

## Cara Menjalankan

1. Pastikan Python 3.x dan modul grafik sudah terinstal (`pip install matplotlib`).
2. Jalankan perintah di terminal: `python nama_file.py`
3. Jendela GUI akan muncul. Masukkan angka pada kolom **Kapasitas Tas**.
4. Klik tombol **Jalankan Algoritma Genetika** dan lihat hasilnya di layar.
