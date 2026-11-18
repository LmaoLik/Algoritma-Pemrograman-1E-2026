# Tiga set awal kosong
undangan = set()
webinar_a = set()
webinar_b = set()

def isi_set(nama_set, label):
    while True:
        try:
            data = input(f"Masukkan {label} (pisahkan dengan koma): ")

            hasil = {n.strip() for n in data.split(",") if n.strip()}
            
            if any(c.isdigit() for c in data):
                print("Input ditolak! Nama tidak boleh mengandung angka.\n")
                # raise ValueError("Nama tidak boleh mengandung angka.")
            elif not hasil:
                # raise ValueError("Nama tidak boleh kosong.")
                print("Input ditolak! Nama tidak boleh kosong.\n")
            else:
                nama_set.update(hasil)
            break
        except ValueError:
            print(f"Input ditolak! Terjadi kesalahan, Nama tidak boleh kosong atau mengandung angka. Silakan coba lagi.\n")

# Isi ketiga set lewat input pengguna
isi_set(undangan, "daftar undangan")
isi_set(webinar_a, "peserta Webinar A")
isi_set(webinar_b, "peserta Webinar B")

# Operasi himpunan
semua_peserta = webinar_a | webinar_b                 # union
hadir_di_keduanya = webinar_a & webinar_b             # intersection
hanya_salah_satu = webinar_a ^ webinar_b              # symmetric difference
tidak_hadir = undangan - (webinar_a | webinar_b)      # difference

# Tampilkan hasil
print("\n=== HASIL ===")
print("Semua peserta dari kedua webinar :", sorted(semua_peserta))
print("Peserta hadir di keduanya        :", sorted(hadir_di_keduanya))
print("Peserta hanya di salah satu      :", sorted(hanya_salah_satu))
print("Undangan tidak hadir di mana pun :", sorted(tidak_hadir))