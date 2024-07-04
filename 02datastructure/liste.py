# lista_mea = []
# print(type(lista_mea))
# lista_mea = [8, 20, 'Ana are mere', 5, 'pere', 34, 20, 89, "struguri", False]
# print(lista_mea[0+4])
# print(lista_mea[5])
# print(lista_mea[-4])
# print(lista_mea[0:3])  # [0, 3)
# print(lista_mea[0:8])
# print(lista_mea[0:8])
# print(lista_mea[0:8:3])
# print(lista_mea[2:])
# print(lista_mea[:2])
# print(len(lista_mea))
# print(lista_mea.index(20))
# print(lista_mea.index(89))
# lista_mea.append("pepene")
# print(lista_mea)
# print(lista_mea.index("pepene"))
# lista_mea.insert(2, "pepene")
# print(lista_mea)
# lista_mea.remove(34)
# lista_mea.remove(20)
# print(lista_mea[6])
# print(lista_mea)
# lista_mea.pop(2)
# print(lista_mea)
# lista_mea.clear()
# lista_mea.reverse()
# print(lista_mea.count(20))
# print(lista_mea)

lista_mea = [8, 20, 'Ana are mere', 5, 'pere', 34, 20, 89, "struguri", False]
lista_voastra = [100, True, "pepene"]
# lista_noua = lista_mea + lista_voastra
# lista_noua = lista_voastra + lista_mea
# print(lista_noua)
lista_mea.extend(lista_voastra)
print(lista_mea)
