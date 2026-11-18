jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

while jumlah_baris <= 0 or jumlah_lampu <= 0:
    print("Input tidak valid! Masukkan bilangan positif (lebih dari 0).\n")
    jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
    jumlah_lampu = int(input("Masukkan jumlah lampu pada setiap baris: "))

for baris in range(1, jumlah_baris + 1):
    print("\n== Baris", baris, "==")

    for lampu in range(1, jumlah_lampu + 1):
        if lampu % 3 == 0:
            print("Lampu", lampu, "pada baris", baris, "mengalami gangguan")
        else:
            print("Lampu", lampu, "pada baris", baris, "berfungsi normal")

print("\nSemua lampu sudah diperiksa.")
print("Silakan periksa sumber listrik utama taman.")