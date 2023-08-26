import random

# Operadores lógicos
# Mayor que >
# Menor que <
# Mayor o igual que >=
# Menor o igual que <=
# Igual que ==
# Distinto de !=
# Negación !


numero = input("Introduce un número: ")

if not numero:
    numero = random.randint(-10, 10)
elif numero != '':
    numero = int(numero)

print(numero)
if numero > 5 and numero < 10:
    print("El número está entre el 5 y el 10")
elif numero < 0 and numero > -10:
    print("El número está entre -10 y 0")
elif numero == 10 or numero == 5 or numero == 0 or numero == -10:
    print('Este numero es especial')
else:
    print('Este número no es especial')