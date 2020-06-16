# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename): 
    shares = 0
    price = 0
    total = 0
    f = open(filename)
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = row[1]
        price = row[2]
        total += float(price) * int(shares)
    f.close()
    return total
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost: ', cost)
