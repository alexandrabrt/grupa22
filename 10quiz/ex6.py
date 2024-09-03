"""
Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7].
Sa se insereze in acest sir dupa fiecare element par, dublul acestuia (2 puncte)
result = [1, 2, 4, 3, 4, 8, 5, 6, 12, 7]
"""
sir_numere = [1, 2, 3, 4, 5, 6, 7]
sir_final = []
for i in range(len(sir_numere)):
    if sir_numere[i] % 2 == 0:
        sir_final.append(sir_numere[i])
        sir_final.append(sir_numere[i] * 2)
    else:
        sir_final.append(sir_numere[i])
print(sir_final)


#rezolvare2

def par_duble(lista: list) -> list:
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            lista.insert(i+1, lista[i] * 2)
            i += 1
        i += 1
    return lista
