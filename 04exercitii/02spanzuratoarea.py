# avem vizibile doar litera de inceput si litera de final
# daca aceste litere se repeta in interiorul cuvantului atunci sunt si ele vizibile
# restul literelor sunt ascunse, le afisam cu _
# avem 7 vieti
cuvant = "onomatopee".lower()  # o _ o _ _ _ _ _ e e
cuvant_de_ghicit = list(cuvant)
# pas 1: inlocuim literele care nu se afla la inceput sau sfarsit de cuvant cu _
for index, valoare in enumerate(cuvant):
    # daca litera de inceput este diferita cu valoarea iterata si
    # litera de final e diferita cu valoarea iterata, adaugam _
    if cuvant[0] != valoare and cuvant[-1] != valoare:
        cuvant_de_ghicit[index] = '_'
cuvant_de_ghicit = ' '.join(cuvant_de_ghicit)
print(cuvant_de_ghicit)
numar_vieti = 7
# pas 2: oferim utilizatorului posibilitatea de a spune litere pentru ghicire cuvant
while numar_vieti > 0:
    litera = input("Alege o litera: ").lower()
    # daca utilizatorul introduce mai multe caractere, afisam pe ecran eroare
    if len(litera) > 1 or litera in '0123456789':
        print("Introduceti o singura litera si nu cifre")
        continue
    elif litera in cuvant:
        # daca litera se afla in cuvant, atunci o inlocuim
        cuvant_de_ghicit = list("".join(cuvant_de_ghicit).replace(" ", ""))
        for index, valoare in enumerate(cuvant):
            # daca litera introdusa este egala cu litera iterata din cuvant
            if litera == valoare:
                cuvant_de_ghicit[index] = litera
        cuvant_de_ghicit = ' '.join(cuvant_de_ghicit)
        print(cuvant_de_ghicit)
        if "".join(cuvant_de_ghicit) == cuvant or "_" not in cuvant_de_ghicit:
            print(f"Ai castigat! Cuvantul era: {cuvant}")
            break
    else:
        numar_vieti = numar_vieti - 1
        if numar_vieti <= 0:
            print(f"Ai pierdut! Cuvantul era: {cuvant}")


