nama = []
akhir = []
kategori = []

for i in range(10):
    print("\nMahasiswa ke-" + str(i + 1))
    n = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    nilai = tugas * 0.30 + uts * 0.30 + uas * 0.40

    if nilai >= 85:
        k = "A"
    elif nilai >= 75:
        k = "B"
    elif nilai >= 65:
        k = "C"
    elif nilai >= 50:
        k = "D"
    else:
        k = "E"

    nama.append(n)
    akhir.append(nilai)
    kategori.append(k)

    print("Nilai Akhir :", round(nilai, 2), "| Kategori :", k)

print("\n= JUMLAH PER KATEGORI =")
for k in ["A", "B", "C", "D", "E"]:
    print("Kategori", k, ":", kategori.count(k), "mahasiswa")

print("\n= STATISTIK =")
print("Tertinggi :", round(max(akhir), 2), "(" + nama[akhir.index(max(akhir))] + ")")
print("Terendah  :", round(min(akhir), 2), "(" + nama[akhir.index(min(akhir))] + ")")
print("Rata-rata :", round(sum(akhir) / 10, 2))