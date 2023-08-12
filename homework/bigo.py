import datetime

# var = 0
start_date = datetime.datetime.now()
print('Inicio: ', start_date)

total = 0

for i in range(1, 1001):
    total += i
    for j in range(1, 1001):
        total += i * j
        for k in range(1, 1001):
            total += k

print('Fin: ', datetime.datetime.now() - start_date)
