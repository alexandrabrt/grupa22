"""
sa se acceseze o valoare intr-un dictionar dupa cheia specificata de utilizator.
Folosim try-except pentru a gestiona cazul in care cheia nu exista in dictionar
"""
dictionar = {'Angajat1': 1, 'Angajat2': 2, 'Angajat3': 3}

try:
    cheie = input("Introduceti angajatul pentru care doriti sa vizualizati numar de zile de concediu: ").capitalize()
    print(dictionar[cheie])
except KeyError:
    print('Angajatul nu exista. Acesta este un angajat nou. Adaugati nr de zile de concediu')
    dictionar[cheie] = 21
    print(dictionar[cheie])
    print(dictionar)
# print(dictionar.get(cheie))
