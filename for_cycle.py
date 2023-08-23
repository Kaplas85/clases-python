mercado = ["mantequilla", "huevos", "aceite"]

for item in mercado:
    print(item + "X")

mercado = [
    {
        "nombre": "mantequilla",
        "precio": 23
    },
    {
        "nombre": "huevos",
        "precio": 10
    },
    {
        "nombre": "harina",
        "precio": 5
    }
]

for item in mercado:
    print(item["precio"])

some_item = {
    "nombre": "harina",
    "precio": 5
}

for clave, valor in some_item.items():
    print(valor)