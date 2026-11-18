# Data awal
uang_awal = 200000
jumlah_buku = 3
harga_buku = 25000
jumlah_pulpen = 2
harga_pulpen = 8000
jumlah_flash_disk = 1
harga_flash_disk = 75000

# Perhitungan
total_buku = jumlah_buku * harga_buku
total_pulpen = jumlah_pulpen * harga_pulpen
total_flash_disk = jumlah_flash_disk * harga_flash_disk
total_kotor = total_buku + total_pulpen + total_flash_disk
besar_diskon = 0.10 * total_kotor
harga_diskon = total_kotor - besar_diskon
besar_pajak = 0.11 * harga_diskon
total_bayar = harga_diskon + besar_pajak
kembalian = uang_awal - total_bayar

# Output
print("Total Buku :", total_buku)
print("Total Pulpen :", total_pulpen)
print("Total Flash Disk :", total_flash_disk)
print("Total Kotor :", total_kotor)
print("Diskon 10% :", besar_diskon)
print("Harga setelah diskon :", harga_diskon)
print("Pajak 11% :", besar_pajak)
print("Total Bayar :", total_bayar)
print("Kembalian :", kembalian)