def palindrom(kata):
    for i in range(len(kata) // 2):
        if kata[i] != kata[len(kata) - 1 - i]:
            return False
    return True


kata = input("Masukkan kata: ")

if palindrom(kata):
    print("Kata", kata, "adalah palindrom")
else:
    print("Kata", kata, "bukan palindrom")