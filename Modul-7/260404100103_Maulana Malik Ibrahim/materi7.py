mahasiswa = {"Nama":"speed", "NIM":"1234567890", "Jurusan":"Teknik Informatika", "Fakultas":"Ilmu Komputer"}
# print(mahasiswa)
mahasiswa["mata kuliah"] = "Pemrograman Python"

mahasiswa2 = dict(Nama="kaicenat", NIM="0987654321", Jurusan="Teknik Mesin", Fakultas="Teknik")
# del mahasiswa["mata kuliah"]
mahasiswa.clear()
for key, value in mahasiswa2.items():
    print(f"{key}: {value}")