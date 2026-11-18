penuh = 0

for i in range(10):
    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    gaji = int(input("Penghasilan orang tua: "))

    if ipk < 3.00:
        print(nama, "- tidak memenuhi syarat\n")
        continue

    if gaji <= 3000000:
        print(nama, "- beasiswa penuh\n")
        penuh += 1
    elif gaji <= 5000000:
        print(nama, "- beasiswa sebagian\n")
    else:
        print(nama, "- tidak mendapat beasiswa\n")

    if penuh == 3:
        print("Kuota beasiswa penuh terpenuhi, seleksi dihentikan.")
        break