"""
Sa se acceseze un element dintr-o lista dupa indexul specificat de utilizator.
Folosim try-except pentru a gestiona lipsa unui index din lista.
"""
lista = [1, 2, 3, 4, 5]
try:
    valoare_index = int(input("Introduceti indexul: "))
    print(lista[valoare_index])
except IndexError:
    print("Indexul este in afara limitelor listei")
    while valoare_index > len(lista) - 1:
        valoare_index = int(input("Introduceti indexul: "))
    print(lista[valoare_index])

