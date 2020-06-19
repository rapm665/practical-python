# pcost.py
#
# Exercise 1.27
import csv
import sys

'''
Computes the total cost (shares*price) of a portfolio file
'''

def portfolio_cost(filename): 
    try:
        shares = 0
        price = 0
        total = 0
        f = open(filename)
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #i = row.split(',')
            shares = row[1]
            price = row[2]
            total += float(price) * int(shares)
        f.close()
        return total
    except ValueError:
        print("Doesn't look good", line)

if len(sys.argv)== 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: ', cost)
