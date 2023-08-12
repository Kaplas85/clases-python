# edad = int(input("Introduce tu edad: "))

name = input("Introduce tu nombre: ").lower()
age = int(input("Introduce tu edad: "))

# > mayor que
# < menor que
# >= mayor o igual que
# <=  menor igual que
# == igual que
# != distinto de


# if name.lower() == "cesar".lower():
#     print("Puedes pasar")
# elif name.lower() == "adrian".lower():
#     print("Puedes pasar")
# elif name.lower() == "isa".lower():
#     print("Puedes pasar")
# elif name.lower() == "gabo".lower():
#     print("Puedes pasar")

# and (Y)
# or (O)
# not (negación)
# in (dentro)

# if nombre == "cesar" and age >= 18:
#     print(nombre, 'puede pasar')
# else:
#     print('No tiene la mayoria de edad')

allowed = [
    "cesar",
    "gabriel",
    "goyo",
    "cristian"
]

if name in allowed and age >= 18:
    print('Puedes pasar')
else:
    print('No puedes pasar')