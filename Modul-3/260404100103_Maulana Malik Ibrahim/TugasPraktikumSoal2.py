#Minta input sampai valid
n = 0  # nilai awal agar perulangan berjalan

while n < 2 or n > 15:
    n = int(input("Masukkan tinggi setengah menara (2-15): "))
    if n < 2 or n > 15:
        print("Angka harus antara 2 sampai 15. Coba lagi!")


#Cetak bagian atas (membesar)
for k in range(1, n + 1):
    spasi = " " * ((n - k) * 2)
    teks = ""

    # Bagian naik: 1, 2, 3, ... sampai k
    for i in range(1, k + 1):
        teks = teks + str(i % 10) + " "

    # Bagian turun: k-1, ... sampai 1
    for i in range(k - 1, 0, -1):
        teks = teks + str(i % 10) + " "

    print(spasi + teks.strip())


#Cetak bagian bawah (mengecil)
for k in range(n - 1, 0, -1):
    spasi = " " * ((n - k) * 2)
    teks = ""

    # Bagian naik: 1, 2, 3, ... sampai k
    for i in range(1, k + 1):
        teks = teks + str(i % 10) + " "

    # Bagian turun: k-1, ... sampai 1
    for i in range(k - 1, 0, -1):
        teks = teks + str(i % 10) + " "

    print(spasi + teks.strip())