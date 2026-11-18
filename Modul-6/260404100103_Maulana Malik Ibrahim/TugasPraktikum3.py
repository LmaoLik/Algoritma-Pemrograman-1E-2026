def evaluasi(pc):
    ram = int(pc[2])
    if pc[1] == "Normal" and ram >= 8:
        return "Layak"
    return "Tidak Layak"


def jumlah_valid(teks):
    if len(teks) == 0:
        return False
    for huruf in teks:
        if huruf < "0" or huruf > "9":
            return False
    return int(teks) > 0


masukan = input("Jumlah PC yang akan didata: ")
while not jumlah_valid(masukan):
    print("Jumlah tidak valid! Masukkan angka lebih dari 0.")
    masukan = input("Jumlah PC yang akan didata: ")
jumlah = int(masukan)

inventaris = []

for i in range(jumlah):
    print("\nData PC ke-" + str(i + 1))
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    while status != "Normal" and status != "Rusak":
        print("Status tidak valid! Ketik Normal atau Rusak.")
        status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

print("\n Hasil Evaluasi ")
for pc in inventaris:
    try:
        hasil = evaluasi(pc)
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + pc[0] + '", "Status": "' + hasil + '" }')