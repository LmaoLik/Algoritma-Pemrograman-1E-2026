def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas
    
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", tugas)
    print("Nilai UTS      :", uts)
    print("Nilai UAS      :", uas)
    print("Nilai Akhir    :", nilai_akhir)
    print("Grade          :", grade)
    print("Status         :", status)

nama = input("Masukkan nama mahasiswa: ")
while True:
    try:
        tugas = float(input("Masukkan nilai tugas: "))
        while tugas < 0 or tugas > 100:
            print ("Masukkan bilangan dalam 0 sampai 100")
            tugas = float(input("Masukkan nilai tugas: "))

        uts = float(input("Masukkan nilai UTS: "))
        while uts < 0 or uts > 100:
            print("Masukkan bilangan dalam 0 sampai 100")
            uts = float(input("Masukkan nilai UTS: "))

        uas = float(input("Masukkan nilai UAS: "))
        while uas < 0 or uas > 100:
            print("Masukkan bilangan dalam 0 sampai 100")
            uas = float(input("Masukkan nilai UAS: "))
        break
    except ValueError:
        print("nilai harus berupa angka. Silakan masukkan kembali!!")

hitung_nilai(nama, tugas, uts, uas)