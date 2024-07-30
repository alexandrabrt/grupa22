"""
se cere introducerea unui numar pe care dorim sa il convertim in float.
Folosim try-except pentru a trata cazul in care introducem de la tastatura un string.
"""


def verificare_cifre(numar_de_verificat: str) -> bool:
    for i in numar_de_verificat:
        if i not in '0123456789.':
            return False
    return True


try:
    numar = input("Introdu un numar: ")
    numar = float(numar)
    print(numar)
except ValueError:
    print("Nu ati introdus un numar")
    while verificare_cifre(numar) is False:
        numar = input("Introdu un numar: ")
    numar = float(numar)
    print(numar)
