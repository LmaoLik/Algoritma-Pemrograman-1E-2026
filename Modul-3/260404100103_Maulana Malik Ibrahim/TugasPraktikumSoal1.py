penumpang = 0
pendapatan = 0
total_jarak = 0
terjauh = 0

while True:
    jarak = int(input("Jarak (km), 0 untuk selesai: "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid")
        continue

    penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if penumpang % 5 == 0:
        tarif /= 2
        print("Diskon 50%!")

    print("Tarif: Rp", tarif)

    pendapatan += tarif
    total_jarak += jarak
    if jarak > terjauh:
        terjauh = jarak

if penumpang == 0:
    print("Tidak ada penumpang.")
else:
    print("Jumlah penumpang :", penumpang)
    print("Total pendapatan : Rp", pendapatan)
    print("Jarak terjauh    :", terjauh, "km")
    print("Rata-rata jarak  :", total_jarak / penumpang, "km")