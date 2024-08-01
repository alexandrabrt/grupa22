"""
r -> citire, nu adauga, este valoarea default, daca fisierul
    nu exista apare eroare
w -> scriere, daca fisierul nu exista, il adauga,
    daca exista informatie in fisier, aceasta este rescrisa
a -> scriere, daca exista informatie in fisier, adauga, nu rescrie
r+ -> scriere, citire, daca fisierul nu exista, apare eroare
"""
# file = open('data.txt', 'r+')
# file.write("hello\n")
# file.close()
#
# file = open('data.txt', 'a')
# file.write("hello1\n")
# file.close()
# with open('data.txt', 'w') as file:
#     file.write("hello")

# with open("data.txt", 'r') as file:
#     # print(file.readlines())
#     text = file.readlines()
#     print(text)
#     for line in text:
#         print(line)

# with open('data.txt', 'r') as file:
#     # print(list(file))
#     for line in list(file):
#         print(line)

with open('data.txt', 'r') as unicorn:
    while True:
        line = unicorn.readline()
        if not line:
            break
        print(line)
