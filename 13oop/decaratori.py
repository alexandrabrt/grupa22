class Animal:
    specie = 'Animal'

    @classmethod
    def set_specie(cls, specie_noua):
        cls.specie = specie_noua


print(Animal.specie)
Animal.set_specie("Mamifer")
print(Animal.specie)
obiect = Animal()
obiect.set_specie("pasare")
print(obiect.specie)
