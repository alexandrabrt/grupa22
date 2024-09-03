"""
Scrieti o functie, care sa separe o lista data de utilizator,
in doua parti, astfel incat lungimea primei liste sa fie egala cu un numar dat.
model:
list_example = [1, 1, 2, 3, 4, 4, 5, 1]
first_list_length = 3
result = ([1, 1, 2], [3, 4, 4, 5, 1])
(1 punct)
"""


def separare_lista(slice_point: int, lista_initiala: list) -> tuple:
    lista1 = lista_initiala[:slice_point]
    lista2 = lista_initiala[slice_point:]
    return lista1, lista2


lista_utilizator= [int(caracter) for caracter in input("Introduceti lista dorita:\n").split(",")]

print(lista_utilizator)
numar_separare = int(input("Introduceti punctul de separare:\n"))
print(separare_lista(numar_separare,lista_utilizator))
