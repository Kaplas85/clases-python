# some_string = "Some random text"
# print(some_string, type(some_string))

# some_string = list(some_string)
# print(some_string, type(some_string))

market = ["huevos", "mantequilla", "harina", "doritos", "panelas"]
print(market)
print('Longitud inicial', len(market))

market.append("mayonesa")
print(market)

market.insert(10, "jabon")
print(market)

# Manera 1 de eliminar un item
market.remove("doritos")
print(market)

# Manera 2 de eliminar un item
market.pop(1)
market.pop(2)
print(market)

print('Longitud final', len(market))

market.reverse()
print(market)

age = [15, 18, 32, 20, 50]
age.sort()
print(age)