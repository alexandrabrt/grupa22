def check_type(operator: str) -> (bool, str):
    stare_conversie = True
    for element in operator:
        if element not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            stare_conversie = False
            break
    return stare_conversie, operator


def check_operand(operand: str) -> str:
    if len(operand) == 1 and operand in '+-*/':
        return operand


def conversie_operator(operator_de_convertit: bool,
                       valoare_de_convertit: str) -> float:
    if operator_de_convertit is True:
        return float(valoare_de_convertit)


def functie_matematica(numar_1: float, numar_2: float,
                       operatie_matematica: str) -> str:
    if operatie_matematica == '+':
        rezultat = "Suma nu se poate realiza"
    else:
        rezultat = "Diferenta nu se poate realiza"
    if numar_1 and numar_2:
        if operatie_matematica == '+':
            valoare_operatie = numar_1 + numar_2
        else:
            valoare_operatie = numar_1 - numar_2
        rezultat = f"{numar_1} {operatie_matematica} {numar_2} = {valoare_operatie}"
    return rezultat


def functie_diferenta(numar_1: float, numar_2: float) -> str:
    rezultat = "Diferenta nu se poate realiza"
    if numar_1 and numar_2:
        rezultat = f"{numar_1} - {numar_2} = {numar_1 - numar_2}"
    return rezultat


stare_conversie_1, operator_1 = check_type(input("Primul operator: "))
stare_conversie_2, operator_2 = check_type(input("Al doilea operator: "))
operatie = check_operand(input("Alege operatorul: "))
valoare_1 = conversie_operator(stare_conversie_1, operator_1)
valoare_2 = conversie_operator(stare_conversie_2, operator_2)
print(functie_matematica(valoare_1, valoare_2, operatie))
