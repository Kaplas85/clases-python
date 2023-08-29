registro_estudiantes = []

while True:
    nombre = input("Introduce un nombre: ").lower()

    if nombre == "exit":
        break

    apellido = input("Introduce un apellido: ").lower()

    estudiante = (nombre, apellido)

    registro_estudiantes.append(estudiante)

    print("\n"+"-"*40)
    print(f'El estudiante {estudiante[0]} ya fue registrado.')
    print("-"*40 + "\n")


print("\n"+"-"*40)
for nombre, apellido in registro_estudiantes:
    print(f'ESTUDIANTE: {nombre} {apellido}')
print("-"*40 + "\n")