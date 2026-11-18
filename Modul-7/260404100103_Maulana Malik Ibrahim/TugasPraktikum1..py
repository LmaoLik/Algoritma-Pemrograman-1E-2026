todo = {}

while True:
    # print(f"\n1. Tambah  2. Tampilkan  3. Selesai  4. Hapus  5. Statistik  0. Keluar")
    print("\n TO DO LIST")
    print("1. Tambah")
    print("2. Tampilkan")
    print("3. Selesai")
    print("4. Hapus")
    print("5. Statistik")
    print("0. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        nama = input("Nama tugas: ")
        todo[nama] = "Belum"
        if not nama.strip():
            print("Nama tugas tidak boleh kosong.")
    elif menu == "2":
        for nama, status in todo.items():
            print(f"- {nama}: {status}")
        if not todo:
            print("Belum ada tugas.")
    elif menu == "3":
        nama = input("Tugas yang selesai: ")
        if nama in todo:
            todo[nama] = "Selesai"
        else:
            print("Tugas tidak ditemukan.")
    elif menu == "4":
        nama = input("Tugas yang dihapus: ")
        try:
            del todo[nama]
            print("Tugas dihapus")
        except KeyError:
            print("Tugas tidak ditemukan.")
    elif menu == "5":
        selesai = list(todo.values()).count("Selesai")
        print(f"Selesai: {selesai}, Belum: {len(todo) - selesai}")
    elif menu == "0":
        break
    else:
        print("Pilihan tidak valid.")