students = []

print("*"*10, "\n")
print('Bienvenido a esta mierda de programa. \nSi quieres terminar, solo escribe "n"')
print("\n"+"*"*10)


while True:
    name = input('Nombre del Estudiante: ')

    if name == "n":
        break
    
    age = int(input('Edad del Estudiante: '))

    students.append({
        "name": name, "age": age
    })


print(students)