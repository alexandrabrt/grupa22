# functia lambda

# def suma(x, y):
#     return x + y


# a = suma(1, 2)

# suma = lambda x, y: x + y
# print(suma(1, 2))


# functia map

# def inmultire_la_2(x):
#     return x * 2

# inmultire_la_2 = lambda x: x * 2


# list_1 = [1, 5, 4, 6, 8, 11, 3, 12]

# list_3 = list(map(lambda x: x * 2, list_1))
# list_3 = list(map(inmultire_la_2, list_1))
# print(list_3)


# def iterare(x: list) -> list:
#     lista_noua = []
#     for i in x:
#         lista_noua.append(i * 2)
#     return lista_noua
#
#
# a = iterare(list_1)
# print(a)


# filter
# list_1 = [1, 5, 4, 6, 8, 11, 3, 12]

# list_2 = list(filter(lambda x: x % 2 != 0, list_1))
# print(list_2)


# def filtrare(x: list) -> list:
#     lista_forloop = []
#     for i in x:
#         if i % 2 == 0:
#             lista_forloop.append(i)
#     return lista_forloop
#
#
# list_2 = filtrare(list_1)
# print(list_2)


# zip
# lista_intregi = [1, 2, 3, 4, 5, 6]
# lista_stringuri = ('unu', 'doi', 'trei', 'patru', 'cinci', 'sase')
# lista_float = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
#
# # rezultat = list(zip(lista_intregi, lista_stringuri, lista_float))
# rezultat = 0
# for x, y in list(zip(lista_intregi, lista_float)):
#     rezultat = x * y + rezultat
# print(rezultat)

# var = 'comprehension'
# print(list(var))
# list_for_loop = []
# for caracter in var:
#     list_for_loop.append(caracter)
# print(list_for_loop)
# list_for_loop = [caracter for caracter in var]
# print(list_for_loop)

# numbers_list = []
# for x in range(30):
#     if x % 2 == 0:
#         numbers_list.append(x)
# numbers_list = [x for x in range(30) if x % 2 == 0]
# print(numbers_list)

# numbers_list = []
# for x in range(30):
#     if x % 2 == 0:
#         numbers_list.append(x)
#     else:
#         numbers_list.append(0)
# numbers_list = [x if x % 2 == 0 else 0 for x in range(30)]
# print(numbers_list)


# dictionar = {}
#
# for i in range(1, 11):
#     dictionar[i] = i * i
# dictionar = {i: i * i for i in range(1, 11) if i % 2 == 0}
# dictionar = {i: i * i if i % 2 == 0 else 0 for i in range(1, 11)}
# print(dictionar)

#
# my_numbers = {2, 5, 3, 5, 4, 1, 2}
# doubled = len(my_numbers) * 2
# print(doubled)
"""
a. TypeError
b. 10
c. 14
d. 12
"""

# var_1 = [x for x in range(20) if x / 2 == 0]
# print(var_1)
"""
a. [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
b. [2]
c. [0]
d. [0, 1]
"""

# char = 'cha'
# cha = 'char'
# print(len(char) * 'cha')
"""
a. charcharcharchar
b. chachachacha
c. chachacha
d. charcharchar
"""

# var = 1
# while var < 4:
#     for var in range(4):
#         if var == 1:
#             var = var + 1
#             break
#         print('var = 4')
#     var = var + 1
# print(var + 1)
"""
a. 2
b. var = 4
    2
c. var = 4
   var = 4
   var = 4
   2
d. infinite loop
"""

# new_str = "Py'th\\'on"
# print(new_str[::-1])
"""
a. Py'th'on
b. no'\\ht'yP
c. Py'th\\'on
d. no'\ht'yP
"""

# planets = [['Mercury', 'Venus', 'Earth'],
#            ['Mars', 'Jupiter', 'Saturn'],
#            ['Uranus', 'Neptune', 'Pluto']]
#
# flatten_planets = []
# for sublist in planets:
#     for planet in sublist:
#         if len(planet) < 6:
#             flatten_planets.append(planet)
# print(flatten_planets)
"""
a. [5, 4, 5]
b. ['V','e','n','u','s',  'M','a','r','s',  'P','l','u','t','o']
c. ['Venus', 'Earth', 'Mars', 'Pluto']
d. ['Venus', 'Mars', 'Pluto']
"""
# var_1 = ['abc', 'def', 'ghi']
# for item in var_1:
#     if type(item) == 'str':
#         item.upper()
#     else:
#         item.title()
# print(var_1)
"""
a. None
b. ['ABC', 'DEF', 'GHI']
c. ['abc', 'def', 'ghi']
d. ['Abc', 'Def', 'Ghi'
"""


# def double_number(n):
#     return lambda x: x * n


# result = double_number(5)
# result = lambda x: x * 5
# print(result(3-1))
"""
a. 4
b. 10
c. Error
d. None
"""

# new_dict = {'item_1': 2, 'item_3': 1, 'item_2': 3}
# result = list(new_dict.keys()) + list(new_dict.values())
# print(str(result))
"""
a. ['item_1', 'item_3', 'item_2']
b. "['item_1', 'item_3', 'item_2', 2, 1, 3]"
c. "item_1, item_3, item_2, 2, 1, 3"
d. Error
"""


# def new_function(x, y) -> str:
#     new_result = x * 2 + y
#     if new_result % 2 != 0:
#         print("Not even")
#     else:
#         return 'Orice'
#
#
# print(new_function(2, 3))
"""
a. Not even
   None
b. Not even
c. Error
d. None
"""


# def my_function():
#     l = list()
#     for i in range(1, 4):
#         l.append(i**2)
#     print(l)
#
#
# my_function()
"""
a. [1, 4, 9, 16]
b. [1, 4, 9]
c. [1, 2, 6]
d. [ ]
"""

var_obj = {'key_1': "val_1",
           "val_2": "key_2",
           "key_3": "val_3"}
# var_obj['key_2'] = 'val_2'
var_obj.update({'key_2': 'val_2'})
print(var_obj)
"""
a. {'key_1': 'val_1',  'key_2': val_2', 'key_3': 'val_3'}
b. {'key_1': 'val_1',  'val_2': val_2', 'key_3': 'val_3'} 
c. KeyError
d. {'key_1': 'val_1',  'val_2': 'key_2',  'key_3': 'val_3',  'key_2': 'val_2'}
"""
