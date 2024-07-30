my_var = input("Adauga un numar: ")
try:
    conversie_int = int(my_var)
    a = int(input("a doua valoare: "))
    impartire = conversie_int / a
    print(variabila)
except ValueError:
    print("eroare de valoare")
except NameError:
    print('variabila nu este declarata')
    variabila = None
except ZeroDivisionError:
    print("Impartirea la zero nu este permisa")
    while a == 0:
        a = int(input("A doua valoare: "))
    impartire = conversie_int / a
    print(impartire)
except Exception as e:
    print(e)
else:
    print("Codul nu are exceptii")
finally:
    print("se executa indiferent")
print(variabila)
