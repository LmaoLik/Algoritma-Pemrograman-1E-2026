# DATA:
jarak_rumah_keluarga = 100  #kilometer
konsumsi_bensin_dimas = 40 #kilometer per liter
sisa_bensin_awal = 1.5 #liter
harga_bensin = 10000 #rupiah per liter

# PROSES:
# karena dimas memutuskan untuk PP, maka jarak yang ditempuh adalah 2 kali jarak rumah keluarga
jarak_tempuh = 2 * jarak_rumah_keluarga
total_bensin_yang_diperlukan = jarak_tempuh / konsumsi_bensin_dimas
total_bensin_yang_dibeli = total_bensin_yang_diperlukan - sisa_bensin_awal


total_biaya_bensin = total_bensin_yang_dibeli * harga_bensin

print (f"jarak total yang ditempuh dimas = {jarak_tempuh} km")
print (f"total bensin untuk seluruh perjalanan = {total_bensin_yang_diperlukan} liter")
print (f"total bensin yang harus dibeli = {total_bensin_yang_dibeli} liter")
print (f"total biaya bensin = {total_biaya_bensin} rupiah")
