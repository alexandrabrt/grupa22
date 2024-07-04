# my_var = 7
# if my_var > 6:
#     print("Set instructiuni 1")
# elif my_var > 8:
#     print("Set instructiuni 3")
# elif my_var <= 5:
#     print("Set instructiuni 4")
# else:
#     print("Set instructiuni 2")

# salariu, nivel_salariu = 2, None
# salariu = 2
# nivel_salariu = "Salariul este mic"
# if salariu > 4:
#     nivel_salariu = "Salariul este mare"
# elif salariu == 3:
#     nivel_salariu = "Salariul este mediu"
# print(nivel_salariu)
# nivel_salariu = "Salariul este mare" if salariu > 4 else "Salariul este mic"
# print(nivel_salariu)
salariu_brut = None
salariu = 2
nivel_salariu = "Salariul este ok"
if (salariu_net := salariu + 2) and salariu_net > 4 and (salariu_brut := salariu_net - 2):
    nivel_salariu = f"Salariul este mare si salariul brut are valoarea {salariu_brut}"
elif (salariu_net := salariu + 1) and salariu_net >= 3:
    nivel_salariu = "Salariul este mediu"
print(nivel_salariu)
print(salariu_brut)
