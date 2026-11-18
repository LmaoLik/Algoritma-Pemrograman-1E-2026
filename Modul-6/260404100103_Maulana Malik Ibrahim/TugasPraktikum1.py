def ada_angka(nama):
    for huruf in nama:
        if "0" <= huruf <= "9":
            return True
    return False


daftar = []
while True:
    nama = input("Masukkan nama (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    elif ada_angka(nama):
        print("Nama tidak boleh mengandung angka!")
    elif len(nama) > 20:
        print("Nama tidak boleh lebih dari 20 karakter!")
    else:
        daftar.append(nama)

print("\n Hasil Evaluasi ")
for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid!")
    else:
        print(nama, "valid.")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")
try:
    daftar.remove(penyusup)
    print(penyusup, "berhasil dihapus.")
except ValueError:
    print(penyusup, "tidak ditemukan di pendaftaran.")

print("\n Daftar Anggota Akhir ")
for nama in daftar:
    print(nama)