cart = []
total = 0

print("*"*10, "\n")
print('Bienvenido a esta mierda de programa. \nSi quieres terminar, solo escribe "n"')
print("\n"+"*"*10)


while True:
    name = input('Nombre del Producto: ')

    if name == "n":
        break
    
    price = float(input('Precio del Producto: '))

    cart.append({
        "name": name, "price": price
    })

    total += price


print(cart, total)