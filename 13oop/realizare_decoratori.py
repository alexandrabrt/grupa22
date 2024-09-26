# def decorator_simplu(functie_decorata):
#     print(f"Apelam functia {functie_decorata.__name__}")
#     return "True"
#
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"


# print(functie_simpla())

# import time

# def decorator_depozite(functie_decorata):
#     def ambalaj_metoda(parametru_functie):
#         return f"Ambalam produse din {functie_decorata.__name__} care contine cartea {parametru_functie}"
#     return ambalaj_metoda
#
#
# @decorator_depozite
# def impachetare_carti(nume):
#     return nume
#
#
# print(impachetare_carti("Ion"))

# def decorator_depozite(material):
#     def ambalaj(denumire_functie):
#         def ambalaj_intern(carte):
#             return f"Ambalam produse din {denumire_functie.__name__} cu materialul {material} care contine cartea {carte}"
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozite("hartie")
# def impachetare_carti(nume):
#     return nume


# print(impachetare_carti("Ion"))

# def decorator_depozite(material):
#     def ambalaj(denumire_functie):
#         def ambalaj_intern(*carte):
#             return f"Ambalam produse din {denumire_functie.__name__} cu materialul {material} care contine cartile {', '.join(carte)}"
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozite("hartie")
# def impachetare_carti(*nume):
#     return nume


# print(impachetare_carti("Ion", "Baltagul"))


# def decorator_depozite(material):
#     def ambalaj(denumire_functie):
#         def ambalaj_intern(nume_autor, prenume_autor):
#             return f"Ambalam produse din {denumire_functie.__name__} cu materialul {material} ale autorului {prenume_autor} {nume_autor}"
#         return ambalaj_intern
#     return ambalaj
#
#
# @decorator_depozite("hartie")
# def impachetare_carti(nume, prenume):
#     return nume, prenume


# print(impachetare_carti("Eminescu", "Mihai"))


# def decorator_simplu(functie_decorata):
#     print(f"Apelam functia {functie_decorata.__name__}")
#     return functie_decorata
#
#
# @decorator_simplu
# def functie_simpla():
#     return "Buna seara"
#
#
# print(functie_simpla())



# def decorator_depozite(functie_decorata):
#     def ambalaj_metoda(parametru_functie):
#         print(f"Ambalam produse din {functie_decorata.__name__} care contine cartea {parametru_functie}")
#         return functie_decorata(parametru_functie)
#     return ambalaj_metoda
#
#
# @decorator_depozite
# def impachetare_carti(nume):
#     return nume
#
#
# print(impachetare_carti("Ion"))

import time

# def calculeaza_timpul(functie_decorata):
#     def functie_interioara(param):
#         inceput = time.time()
#         suma = functie_decorata(param)
#         sfarsit = time.time()
#         print(f"Timp total de executie: {sfarsit - inceput}")
#         return suma
#     return functie_interioara
#
#
# @calculeaza_timpul
# def adunare(nr_total):
#     suma = 0
#     for i in range(nr_total):
#         suma += i
#     return suma
#
#
# print(adunare(10))
# print(adunare(50))
# print(adunare(100))
# print(adunare(5000))
#
# @calculeaza_timpul
# def adunare(*args):
#     suma = 0
#     for i in args:
#         suma += i
#     return suma
#
#
# print(adunare(1, 2, 4))


# def requires_permission(permission):
#     def decorator(func):
#         def functie_interna(user, *args, **kwargs):
#             if user.get("role") != permission:
#                 raise PermissionError(f"User does not have {permission} permission")
#             return func(user, *args, **kwargs)
#         return functie_interna
#     return decorator
#
#
# @requires_permission("admin")
# def delete_user(user, username):
#     return f"{username} deleted by {user['name']}"
#
# admin_user = {'name': "Ion", "role": "admin"}
# normal_user = {"name": "Silvia", "role": "user"}
#
# print(delete_user(admin_user, "Cristi"))
# # delete_user(normal_user, "Cristi")

# def nr_apelari(nume_functie):
#     nume_functie.nr_apelari = 0
#
#     def functie_interna(*args, **kwargs):
#         nume_functie.nr_apelari += 1
#         print(f"{nume_functie.__name__} a fost apelata de {nume_functie.nr_apelari} ori")
#         return nume_functie(*args, **kwargs)
#     return functie_interna
#
# @nr_apelari
# def hello():
#     pass
#
# hello()
# hello()
# hello()

import time

def rate_limiter(apeluri_per_secunda):
    interval = 1 / apeluri_per_secunda
    ultima_apelare = [0]

    def decorator(func):
        def functie_interna(*args, **kwargs):
            timp = time.time() - ultima_apelare[0]
            print(timp, interval)
            if timp < interval:
                time.sleep(interval - timp)
            ultima_apelare[0] = time.time()
            return func(*args, **kwargs)
        return functie_interna
    return decorator


@rate_limiter(1)
def send_request():
    print("Request sent")


for i in range(200):
    send_request()
    print(i)
