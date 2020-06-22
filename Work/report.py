# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    '''
    Open and read a portfolio csv file into a list of dictionaries
    '''
    try:
        portfolio = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                holding = {
                        'name' : row[0], 
                        'shares' :  int(row[1]), 
                        'price' : float(row[2])
                        }
                portfolio.append(holding)
        return portfolio
    except ValueError:
        print('Value Error occured', line)

def read_prices(filename):
    '''
    Open and read a price data csv into a dictionary 
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

'''
stock_price_diff = []
gain_loss = {}
for p in portfolio:
    if p['name'] in prices:
        price = prices.get(p['name'],0.0)
        holding = p['price'] - price
        stock_price_diff.append(holding)
        gain_loss[p['name']] = ((p['price'] * p['shares']) - (price * p['shares']))

print('Current stock value changes')
pprint(gain_loss)
'''

total = 0.0
for s in portfolio:
    total += s['shares']*s['price']
print('Portfolio total ',total)

current_total = 0.0
for s in portfolio:
    current_total += s['shares']*prices[s['name']]
print('Current portfolio total ',current_total)
print('Total gain ',current_total - total)
