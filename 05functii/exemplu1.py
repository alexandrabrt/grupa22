# print("Mesaj")
# input("Adauga un numar: ")

def my_function(nr_mere: str = '2', nume: str = "Ioana") -> (str, str):
    """
    :param nr_mere: numarul de mere
    :param nume: numele celui care detine merele
    :return: propozitii
    """
    return f"{nume} are {nr_mere} mere", f"{nume} are {nr_mere} pere"


a, c = my_function('2')
b, d = my_function('3', "Maria")
e, f = my_function(nume='Gelu')
g, h = my_function(nr_mere="6")
print(g, h)
# print(a)
# print(b)
# print(c)
# print(d)
