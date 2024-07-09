operator_1 = input("Primul operator: ")
# verificam daca ceea ce introduce utilizatorul este in intervalul 0-9 sau contine .
stare_conversie = True
for element in operator_1:
    if element not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        stare_conversie = False
        break
if stare_conversie is True:
    operator_2 = input("Al doilea operator: ")
    for element in operator_2:
        if element not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            stare_conversie = False
            break
    # daca putem sa convertim, atunci realizam conversia
    if stare_conversie is True:
        operatie = input("Introdu operatia dorita (+-*/): ")
        operator_1_convertit = float(operator_1)
        operator_2_convertit = float(operator_2)
        # aici putem realiza operatiile
        # daca operatia introdusa de la tastatura se afla in stringul cautat
        if len(operatie) == 1 and operatie in '+-*/':
            rezultat = None
            # daca operatie e + atunci realizam adunare
            # daca operatie e - atunci realizam scadere
            # daca operatie e * atunci realizam inmultire
            # daca operatie e / si operator_2 nu este egal 0 atunci realizam impartire
            if operatie == '+':
                rezultat = operator_1_convertit + operator_2_convertit
            elif operatie == '-':
                rezultat = operator_1_convertit - operator_2_convertit
            elif operatie == '*':
                rezultat = operator_1_convertit * operator_2_convertit
            elif operator_2_convertit != 0.0:
                rezultat = operator_1_convertit / operator_2_convertit
            print(f"{operator_1_convertit} {operatie} {operator_2_convertit} = {rezultat}")
