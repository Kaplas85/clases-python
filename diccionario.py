my_dict = {
    "nombre_usuario": "kaplas",
    "nombre": "cesar",
    "apellido": "baudi",
    "edad": 23
}

# Acceder a una llave
my_dict["nombre_usuario"]

# Reescribir una llave
my_dict["nombre_usuario"] = "john"

# Agregar una llave
my_dict["numero_de_documento"] = "V-00.000.000"

# Eliminar una llave
del my_dict["edad"]

print(my_dict)