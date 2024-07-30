# print(dir(__builtins__))
var = 1
def functie2() -> str:
    global var
    var = 3
    print(var, 'functie2')
    return var
def functie() -> str:
    msg = "Hello"
    print(msg)
    global var
    print(var, 'in functie inainte de reasignare valoare')
    var = 2
    print(var, 'in functia functie')
    return msg

print(var)
functie2()
functie()
print(var, 'global in fisier')

print(locals())
print(globals())
