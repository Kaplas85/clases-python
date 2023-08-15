market_item = {
    "name": "huevo",
    "price": 3,
    "quantity": 15
}

print(market_item)

market_item["name"] = "mantequilla"
print(market_item)

market_item["is_avalible"] = True
print(market_item)

del market_item["is_avalible"]
print(market_item)

print(market_item.keys())
print(market_item.values())
print(market_item.items())


for key, value in market_item.items():
    print(key)
    print(value)