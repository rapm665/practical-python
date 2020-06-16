# pcost.py
#
# Exercise 1.27

shares = 0
price = 0
total = 0
f = open('Data/portfolio.csv', 'rt')
headers = next(f)
for line in f:
    row = line.split(',')
    shares = row[1]
    price = row[2]
    total += float(price) * int(shares)
print('Total cost ', total)
f.close()
