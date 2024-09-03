"""
Scrieti un program care sa afiseze un dictionar ce contine:
- un numar dat de utilizator (numar intreg poztitiv), de chei, cu prima cheie 1
- numarul maxim de chei admise: 20
- valorile pentru fiecare cheie in parte reprezinta patratul cheii (ex. cheie 3 - valoare 9)
(2 puncte)
"""
# rezolvare 1


def nr_de_chei(x: int) -> dict:
    dictionar = {}
    if x < 0:
        print("Numarul trebuie sa fie pozitiv")

    elif x < 21:
        for i in range(1, x + 1):
            dictionar[i] = i * i

        return dictionar
    else:
        print("Numarul maxim este 20")


numar_utilizator = int(input("Introduceti un numar intreg pozitiv intre (1 - 20):\n"))
print(nr_de_chei(numar_utilizator))
