playlist = {}

while True:
    # print("\n1. Buat playlist  2. Tambah lagu  3. Tampilkan semua  4. Cari lagu")
    # print("5. Hapus lagu  6. Hapus playlist  0. Keluar")
    print("\n PLAYLIST MUSIC")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan semua")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("0. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        nama = input("Nama playlist: ")
        if nama in playlist:
            print("Playlist sudah ada.")
        elif not nama.strip():
            print("Nama playlist tidak boleh kosong.")
        else:
            playlist[nama] = {}
    elif menu == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            playlist[nama][judul] = input("Penyanyi: ")
            if not judul.strip() or not playlist[nama][judul].strip():
                print("Judul lagu dan penyanyi tidak boleh kosong.")
        else:
            print("Playlist tidak ditemukan.")
    elif menu == "3":
        for nama, lagu in playlist.items():
            print(f"\n{nama}:")
            for judul, penyanyi in lagu.items():
                print(f"  - {judul} ({penyanyi})")
            if not lagu:
                print("  (kosong)")
        if not playlist:
            print("Belum ada playlist.")
    elif menu == "4":
        cari = input("Judul lagu: ").lower()
        ketemu = False
        for nama, lagu in playlist.items():
            for judul, penyanyi in lagu.items():
                if cari in judul.lower():
                    print(f"'{judul}' oleh {penyanyi} ada di playlist {nama}")
                    ketemu = True
        if not ketemu:
            print("Lagu tidak ditemukan.")
    elif menu == "5":
        nama = input("Nama playlist: ")
        judul = input("Judul lagu: ")
        try:
                del playlist[nama][judul]
                print("Lagu dihapus.")
        except KeyError:
          print("Playlist atau lagu tidak ditemukan.")
         
    elif menu == "6":
        nama = input("Playlist yang dihapus: ")
        if nama in playlist:
            del playlist[nama]
        else:
            print("Playlist tidak ditemukan.")
    elif menu == "0":
        break
    else:
        print("Pilihan tidak valid.")