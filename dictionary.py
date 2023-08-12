cedula_de_identidad = {
    "nombres": ["Cesar", "Andres"],
    "apellido": ["Baudi", "Ventura"],
    "documento": {
        "numero": 28000000,
        "tipo": "V"
    },
    "fecha_expedicion": "1/12/1999"
}

# cedula_de_identidad["fecha_expedicion"] = "11/08/2013"

# print(cedula_de_identidad)

# cedula_de_identidad["documento"]["estado_civil"] = "Soltero"

# print(cedula_de_identidad)

# del cedula_de_identidad["fecha_expedicion"]

# print(cedula_de_identidad)

# print(cedula_de_identidad.keys())
# print(cedula_de_identidad.values())
# print(cedula_de_identidad.items())

for key, value in cedula_de_identidad.items():
    if key == "nombres" and value[0] == "Cesar":
        print('Hola')
