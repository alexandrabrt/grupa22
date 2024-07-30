def functie1():
    def functie2():
        global msg
        msg = 'Hello2'
        print(f"functie secundara: {msg}")
    msg = 'Hello'
    print(f"functie: {msg}")
    functie2()


msg = 'hello3'
print(msg)
functie1()
print(msg)

