direccion = "Venezuela, Puerto Rico, Argentina, Chile, Alemania"
direccion += ", Colombia"
direccion += ", Brazil"

pais_favorito = input("Escribe tu país favorito: ")
ubicacion = direccion.find(pais_favorito)

print("La ubicación de", pais_favorito, "es:", ubicacion)

print("La primera letra de ese país es:", direccion[ubicacion])

