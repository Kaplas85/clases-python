color = input('Introduce un color: ')

match color:
    case "rojo": # if
        print("El pana el chavista")
    case "azul": # elif
        print("El pana es opositor")
    case _:  # else
        print('Ningun color coincide')