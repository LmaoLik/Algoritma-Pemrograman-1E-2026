# KOPERASI NDESO
banyak_barang = int(input("Berapa jenis barang yang dibeli? "))

total_awal = 0

for i in range(banyak_barang):
    print("Barang ke-" + str(i + 1))
    harga = int(input("Harga barang : "))
    jumlah = int(input("Jumlah       : "))
    total_awal = total_awal + (harga * jumlah)

if total_awal % 100000 == 0:
    diskon = 100
elif total_awal % 50000 == 0:
    diskon = 50
elif total_awal % 10000 == 0:
    diskon = 20
elif total_awal >= 200000:
    diskon = 10
else:
    diskon = 0

potongan = total_awal * diskon / 100
total_bayar = total_awal - potongan

status = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
print("Total belanja awal :", total_awal)
print("Diskon             :", diskon, "%")
print("Total bayar        :", total_bayar)
print("Status poin        :", status)
   