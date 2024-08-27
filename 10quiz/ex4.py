"""
Se dă un şir cu cel mult 10 caractere. Să se determine câte vocale conţine. (1 punct)
"""

# rezolvare1


def count_vowel(string):
    vowels = "aeiouAEIOU"
    if len(string) <= 10 and string.isalpha():
        print(sum(string.count(vowel) for vowel in vowels))
    else:
        print("Lungimea sirului de caractere trebuie sa aibe maxim 10 litere")


input_string = str(input("Introduceti un sir de maxim 10 caractere: "))
count_vowel(input_string)

# rezolvare2


def count_vowels() -> str:
    sir = input('Introduceti un sir de maxim 10 caractere: ').lower()
    vowels = 'aeiou'
    count = 0
    if len(sir) <= 10:
        for i in sir:
            if i in vowels:
                count = count + 1
    else:
        return 'Sirul depaseste 10 caractere'
    return str(count)


print(count_vowels())
