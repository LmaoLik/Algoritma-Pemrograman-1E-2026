def pelanggan(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pelanggan(n - 1) + pelanggan(n - 2)

# Program dinamis: hari ke-N diinput oleh pengguna
N = int(input("Masukkan hari ke-N: "))

if N > 0:
    hasil = pelanggan(N)
    print("Jumlah pelanggan pada hari ke-" + str(N) + " adalah", hasil, "orang")
else:
    print("Input harus bilangan bulat positif!")