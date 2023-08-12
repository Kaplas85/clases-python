# Replace

# my_custom_var = "Hola, Cesar"
# print('Antes', my_custom_var)


# my_new_custom_var = my_custom_var.replace(' ', '*')
# print('Despues', my_new_custom_var)


# # Strip
# name = " gabriel "
# print('Antes', name)


# new_name = name.strip()
# print('Despues', new_name)


# Split

# market = "jugo, manzana, pera, mantequilla, mayonesa"
# my_list_market = market.split(',')
# print(my_list_market)

# for item in my_list_market:
#     print(item.strip())


# Format String

# name = "Maria"
# print(f'mi nombre es {name}')

# Constanst

# NAME = "Maria"
# print(NAME)

# NAME = "Cesar"

# "" -> doble quote | comilla doble
# '' -> single quote | comilla simple


name = input('Introduce un nombre: ')

if name == '':
    print(f'El valor que introduciste "nombre" no es valido')
else:
    print(name)