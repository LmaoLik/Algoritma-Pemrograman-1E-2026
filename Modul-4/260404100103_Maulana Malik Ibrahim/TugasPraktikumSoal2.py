total_gaji = 0  # akumulator

for hari in range(1, 8):
    print("\nHari ke", hari)

    lembur = int(input("Jam lembur: "))
    while lembur < 0 or lembur == 5 or lembur == 7:
        print("Jam lembur tidak sesuai ketentuan, masukkan ulang.")
        lembur = int(input("Jam lembur: "))

    if lembur <= 3:
        upah = lembur * 25000
    elif lembur == 4:
        upah = 100000
    elif lembur == 6:
        upah = 200000
    elif lembur == 8:
        upah = 300000
    else:
        print("Jumlah lembur melebihi batas yang ditentukan.")
        upah = 0

    gaji = 100000 + upah
    if input("Shift malam? (y/t): ") == "y":
        gaji += 50000

    print("Gaji hari ini: Rp", gaji)
    total_gaji += gaji

print("\nTotal gaji mingguan: Rp", total_gaji)