import time

# While = mientras

# Enseñanza 1
# Ciclo While modificando condicion
numero = int(input("Escribe un número: ")) # 10

while numero < 32:
    print(f'El número {numero} no es mayor que 32')
    numero += 1


# Enseñanza 2
# Ciclo while con break
while True:
    nombre = input("Introduce un nombre: ")
    print(f"El nombre que introduciste es: {nombre}")

    nombre_lower = nombre.lower()

    if nombre_lower == "exit":
        break
    elif nombre_lower == "cesar":
        continue

    print(f"Buscando nombre en base de datos de la CIA")
    print(f"Buscando antecedentes penales")
    print(f'No se encontro nada relacionado con el nombre {nombre}')
    print('----- FINALIZANDO BUSQUEDA -----')

# Enseñanza 3

# Ciclo While infinito
numero = 0

while True:
    time.sleep(2)
    print(numero)
    numero += 1