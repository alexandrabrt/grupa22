class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def __str__(self):
        return f"{self.nume} {self.prenume} are {self.absente} absente"

    def adauga_absente(self):
        self.absente += 1

    def stergere_absente(self, nr_absente):
        if (total_absente := self.absente - nr_absente) and total_absente > 0:
            self.absente = self.absente - nr_absente

class Extensie1(Catalog):

    def adauga_materie(self, materie, note):
        self.materii[materie] = note
        # self.materii.update({materie: note})

    def afisare_materii(self):
        afisare = f"{self.nume} {self.prenume} are materiile: \n"
        for key in self.materii:
            afisare += f"- {key}\n"
        return afisare

    def afisare_medii(self):
        afisare = f"{self.nume} {self.prenume} are materiile: \n"
        for materie, lista_note in self.materii.items():
            note = [nota for nota in lista_note if isinstance(nota, (int, float))]
            if len(note) == len(lista_note):
                suma = 0
                for i in lista_note:
                    suma += i
                media = suma / len(lista_note)
                afisare += f"- {materie} cu media {media}\n"
            else:
                afisare += f"- Nu exista note valide pentru materia {materie} \n"
        return afisare

student_1 = Extensie1("Ion", "Roata")
student_1.adauga_absente()
student_1.adauga_absente()
student_1.adauga_absente()
# print(student_1)
student_1.stergere_absente(2)
# print(student_1)
student_2 = Extensie1('George', 'Cerc')
student_2.adauga_absente()
student_2.adauga_absente()
student_2.adauga_absente()
student_2.adauga_absente()
# print(student_2)
student_2.stergere_absente(2)
# print(student_2)
student_1.adauga_materie('Python', [6, 7, 8])
student_2.adauga_materie('Python', [3, 7, 9])
student_2.adauga_materie('Matematica', [7, 4, 6])
student_1.adauga_materie('Romana', [4, 9, 10])
# print(student_1.afisare_materii())
# print(student_2.afisare_materii())
print(student_1.afisare_medii())
print(student_2.afisare_medii())
