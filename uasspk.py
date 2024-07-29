# Definisikan Kriteria dan Alternatif

#     Kriteria:
#         Nasab (benefit)
#         Kaya (benefit)
#         Cantik (benefit)
#         Beragama Islam (benefit)

#     Alternatif:
#         Nadya
#         Siti
#         Rani
#         Fitri
#         Lina

# 2. Matriks Keputusan dan Bobot Kriteria

# Misalkan kita memiliki matriks keputusan sebagai berikut:
import numpy as np
import pandas as pd

# Definisikan kriteria dan alternatif
kriteria = ['Nasab', 'Kaya', 'Cantik', 'Beragama Islam']
alternatif = ['Nadya', 'Siti', 'Rani', 'Fitri', 'Lina']

# Matriks keputusan: baris mewakili alternatif dan kolom mewakili kriteria
matriks_keputusan = np.array([
    [8, 7, 6, 10],  # Nadya
    [9, 8, 7, 9],   # Siti
    [7, 9, 8, 10],  # Rani
    [8, 8, 9, 8],   # Fitri
    [10, 9, 7, 9]   # Lina
])

# Bobot kriteria: bobot harus berjumlah 1
bobot = np.array([0.3, 0.3, 0.2, 0.2])

# Normalisasi matriks keputusan
matriks_normalisasi = matriks_keputusan / matriks_keputusan.max(axis=0)

# Menghitung skor akhir untuk setiap alternatif
skor_akhir = matriks_normalisasi.dot(bobot)

# Membuat DataFrame untuk hasil akhir
hasil_akhir = pd.DataFrame({
    'Alternatif': alternatif,
    'Skor Akhir': skor_akhir
})

# Mengurutkan hasil akhir berdasarkan skor dari yang tertinggi ke terendah
hasil_akhir = hasil_akhir.sort_values(by='Skor Akhir', ascending=False)

# Menampilkan hasil akhir
print("Hasil Akhir:")
print(hasil_akhir)

# Rekomendasi alternatif terbaik
alternatif_terbaik = hasil_akhir.iloc[0]['Alternatif']
print(f"\nRekomendasi Alternatif Terbaik: {alternatif_terbaik}")

# Menampilkan hasil normalisasi dan keputusan
print("\nMatriks Normalisasi:")
print(pd.DataFrame(matriks_normalisasi, columns=kriteria, index=alternatif))

print("\nMatriks Keputusan dengan Bobot:")
for i, k in enumerate(kriteria):
    print(f"Kriteria: {k}, Bobot: {bobot[i]}")

# Menampilkan matriks keputusan dengan bobot
print("\nMatriks Keputusan:")
print(pd.DataFrame(matriks_keputusan, columns=kriteria, index=alternatif))

# Menampilkan skor akhir untuk setiap alternatif
print("\nSkor Akhir untuk Setiap Alternatif:")
for i, alt in enumerate(alternatif):
    print(f"{alt}: {skor_akhir[i]}")

# Menampilkan kesimpulan
print("\nKesimpulan:")
print(f"Berdasarkan perhitungan dengan metode SAW, alternatif terbaik adalah {alternatif_terbaik} dengan skor akhir {hasil_akhir.iloc[0]['Skor Akhir']:.6f}.")
