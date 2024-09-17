"""
Max este o pisica mare care doarme toata ziua.
obiect -> Max
clasa -> Pisica
proprietate -> mare
activitate -> doarme (toata ziua)


O masina Dacia rosie merge incet.
obiect: Dacia
clasa: masina
proprietate: rosie
activitate: merge

LIFO -> Last In First Out (ex.: stiva)
FIFO -> First In First Out (ex.: coada de cumparat paine)
"""
stiva = []
def push(val):
    stiva.append(val)
def pop():
    val = stiva[-1]
    del stiva[-1]
    return val
push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())
