pin = int(input("Masukkan 3 digit kode PIN : "))
jam = int(input("Masukkan jam kedatangan (0-23): "))

digit1 = pin // 100          # ratusan
digit2 = (pin // 10) % 10    # puluhan
digit3 = pin % 10            # satuan

print(f"\nDigit pertama : {digit1}")
print(f"Digit kedua   : {digit2}")
print(f"Digit ketiga  : {digit3}")

if pin % 5 == 0:
    if jam < 12:
        status = "Garasi Pagi Terbuka"
    else:
        status = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        status = "Garasi VIP Terbuka Khusus Bos"
    else:
        status = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    status = "Akses Ditolak"

print(f"Status pintu  : {status}")


cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
print(f"Status CCTV   : {cctv}")