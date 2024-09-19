# class Masina:
#
#     def __init__(self, marca, model, an):
#         self.marca = marca
#         self.model = model
#         self.an = an
#
#     def claxoneaza(self):
#         return f"{self.marca} {self.model} claxoneaza!"
#
#
# masina_mea = Masina("Dacia", "Logan", 2020)
# # print(masina_mea.claxoneaza())
# print(masina_mea.marca)

# class ContBancar:
#
#     def __init__(self, nume, sold):
#         self.__sold = sold
#
#     def verificare_sold(self):
#         return self.__sold
#
#
# contul_meu = ContBancar("Ion", 1000)
# # print(contul_meu.verificare_sold())
# print(contul_meu._ContBancar__sold)

# class Exemplu:
#     def __init__(self, val):
#         self.b, self.a = None, None
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#
#
# obiect = Exemplu(2)
# print(obiect.a)

# class Exemplu:
#     varia = 1
#
#     def __init__(self, val):
#         Exemplu.varia = val
#         self.varia = 3
#
#
# obiect = Exemplu(4)
# print(obiect.varia)
# print(Exemplu.varia)
# print(Exemplu.__dict__)
# print(obiect.__dict__)


class Exemplu:
    counter = 0

    def __init__(self, val=1):
        self.first = val
        Exemplu.counter += 1


obiect = Exemplu()
# print(Exemplu.__dict__)
obiect2 = Exemplu(4)
obiect3 = Exemplu(4)

# print(obiect.__dict__)
# print(obiect2.__dict__, Exemplu.__dict__)
# print(hasattr(Exemplu, 'counter'))
# print(hasattr(Exemplu, 'first'))
# print(hasattr(obiect, 'counter'))
# print(hasattr(obiect, 'first'))


# class Animal:
#     def vorbeste(self):
#         print("Animalul scoate un sunet")
#
# class Caine(Animal):
#     def latra(self):
#         print('Cainele latra')
#
# rex = Caine()
# rex.vorbeste()
# rex.latra()

# class Animal:
#     def merge(self):
#         print("Animalul merge")
# class Pasare(Animal):
#     def zboara(self):
#         print('Pasarea zboara')
# class Pinguin(Animal, Pasare):
#     def inoata(self):
#         print('Pinguinul inoata')
#
# pinguin = Pinguin()
# pinguin.merge()

# class A:
#     a = 2
#
#     # def __init__(self):
#     #     self.ab = 4
#     def f(self):
#         print("A.f()")

# class B(A):
#     a = 1
#
#     def __init__(self):
#         self.ab1 = 3
#     def f(self):
#         print("B.f()")
#
# class C(A):
#     pass
#
# class D(B, C):
#     pass
#
# obiect = B()
# # obiect.f()
# # print(obiect.ab)
# print(D.__mro__)

class A:
    def actiune(self):
        self.a = 1
        print("A: actiune")

class B(A):
    def actiune(self):
        self.a = 2
        print("B: actiune")
        super().actiune()

class C(A):
    def actiune(self):
        self.a = 3
        print("C: actiune")
        super().actiune()
class D(B, C):
    def actiune(self):
        self.a = 4
        print("D: actiune")
        super().actiune()

d = D()
d.actiune()
print(d.a)
