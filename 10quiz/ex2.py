"""
Scrieti o functie care sa calculeze suma tuturor numerelor dintr-un tuplu dat.
model:
tuple_example = (8, 2, 3, 0, 7)
result = 20
(1 punct)
"""
# rezolvare 1


def my_sum(my_tuple):
    return sum(my_tuple)


my_tuple_1 = (8, 2, 3, 0, 7)
print(my_sum(my_tuple_1))


# rezolvare 2

def suma_tuplu(x: int, y: int, z: int)-> tuple:
    tuplul_meu=(x,y,z)
    return sum(tuplul_meu)


a,b,c = int(input("Introduceti primul pt tuplu:\n")),int(input("Introduceti al doilea pt tuplu:\n")),int(input("Introduceti al treilea pt tuplu:\n"))
print(suma_tuplu(a,b,c))
