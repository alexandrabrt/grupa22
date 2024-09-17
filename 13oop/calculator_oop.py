class Calculator:

    def __init__(self):
        self.numar1 = self.validare_input(1)
        self.numar2 = self.validare_input(2)
        self.semn = self.validare_operatie()

    def validare_input(self, pozitie):
        if pozitie == 1:
            self.numar1 = input(f"Alege numarul 1: ")
            while self.numar1.isdigit() is False:
                self.numar1 = input(f"Alege numarul 1: ")
            return int(self.numar1)
        elif pozitie == 2:
            self.numar2 = input(f"Alege numarul 2: ")
            while self.numar2.isdigit() is False:
                self.numar2 = input(f"Alege numarul 2: ")
            return int(self.numar2)

    def validare_operatie(self):
        self.semn = input("Adauga semn: ")
        while self.semn not in ['+', '-', '*', "/"]:
            self.semn = input("Adauga semn: ")
        return self.semn

    def adunare(self):
        return self.numar1 + self.numar2

    def scadere(self):
        return self.numar1 - self.numar2

    def inmultire(self):
        return self.numar1 * self.numar2

    def impartire(self):
        while self.numar2 == 0:
            self.numar2 = self.validare_input(2)
        return self.numar1 / self.numar2

    def __str__(self):
        if self.semn == '+':
            return f"{self.numar1} {self.semn} {self.numar2} = {self.adunare()}"
        elif self.semn == '-':
            return f"{self.numar1} {self.semn} {self.numar2} = {self.scadere()}"
        elif self.semn == '*':
            return f"{self.numar1} {self.semn} {self.numar2} = {self.inmultire()}"
        elif self.semn == '/':
            impartire = self.impartire()
            return f"{self.numar1} {self.semn} {self.numar2} = {impartire}"


obiect_calculator = Calculator()
print(obiect_calculator)
