n = int(input("Masukkan bilangan: "))

while n <= 0:
    print("Input tidak valid! Masukkan bilangan positif (lebih dari 0).\n")
    n = int(input("Masukkan bilangan: "))

jarak = 3  # jarak minimum antar piramida (di baris terakhir)

for baris in range(1, n + 1):
    # piramida kiri: 1 sampai baris
    for angka in range(1, baris + 1):
        print(angka, end="")

    # spasi tengah: makin ke bawah makin sempit
    for s in range(jarak + 2 * (n - baris)):
        print(" ", end="")

    # piramida kanan (cermin): baris sampai 1
    for angka in range(baris, 0, -1):
        print(angka, end="")

    print()