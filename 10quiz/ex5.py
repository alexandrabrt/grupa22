"""
Sa se scrie un program care sa calculeze impartirea dintre trei numere.
Daca valorile sunt egale, returnati de trei ori rezultatul.
Impartirea la 0 va duce la rezultatul 0. (1 punct)
"""


def imp_3nr(a, b, c) -> float:

    if a == b == c:
        result = a / b / c
        return result * 3

    elif a == 0 or b == 0 or c == 0:
        return 0

    else:
        result = a / b / c
        return result

print(imp_3nr(2,2,2))
