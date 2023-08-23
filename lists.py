my_list = ["huevos", "mantequilla", "queso", "arroz", "pasta", "aguacate"]


# Agregar algo
my_list.append("mayonesa")
my_list.insert(1, "jamon")

# Eliminar
my_list.remove("queso")
my_list.pop(0)

# Conocer la longitud de mi lista
len(my_list)  # 3

# Ordenar
my_list.sort(reverse=True)

# Voltear
my_list.reverse()

# Buscar indice
print(my_list.index("aguacate"))

## Acceder al contenido de mi lista
my_list[1] = "harina"
print(my_list)


## Slices
# Primer valor -> Inicio
# Segundo Valor -> Fin
# Tercer Valor -> Cantidad de saltos (de cuanto en cuanto)
my_list[0:1:2]