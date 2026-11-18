HARI = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")


def ada_angka(teks):
    for huruf in teks:
        if "0" <= huruf <= "9":
            return True
    return False


def ada(teks, kumpulan):
    for k in kumpulan:
        if teks == k:
            return True
    return False


def input_asisten():
    data = []
    while True:
        x = input("Masukkan nama asisten (ketik 'cukup' untuk berhenti): ")
        if x == "cukup":
            break
        while ada(x, data):
            print("Nama sudah dimasukkan!")
            x = input("Masukkan nama asisten (ketik 'cukup' untuk berhenti): ")
        if ada_angka(x):
            print("Tidak boleh mengandung angka!")
        else:
            data.append(x)
    return tuple(data)


def input_hari():
    data = []
    while True:
        x = input("Masukkan hari tugas (ketik 'cukup' untuk berhenti): ")
        if x == "cukup":
            break
        if not ada(x, HARI):
            print("Hari tidak valid! Gunakan senin sampai minggu.")
        elif ada(x, data):
            print("Hari sudah dimasukkan!")
        else:
            data.append(x)
    return tuple(data)


asisten_awal = input_asisten()

tambahan = input("Masukkan nama asisten tambahan: ")
while ada_angka(tambahan):
    print("Tidak boleh mengandung angka!")
    tambahan = input("Masukkan nama asisten tambahan: ")

asisten_akhir = asisten_awal + (tambahan,)

hari = input_hari()

ex_asisten = input("\nNama asisten pengecualian: ")
ex_hari = input("Hari pengecualian: ")
while not ada(ex_hari, HARI):
    print("Hari tidak valid! Gunakan senin sampai minggu.")
    ex_hari = input("Hari pengecualian: ")

print("\n Jadwal Shift ")
for a in asisten_akhir:
    for h in hari:
        if a != ex_asisten or h != ex_hari:
            print(a, "-", h)