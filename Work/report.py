# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    #total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'NAME: ' row[0], 
                        'SHARE: ' int(row[1]), 
                        'PRICE: ' float(row[2])
                      }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}
    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = row[1]
        except IndexError:
            pass
    return 
    
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

for s in portfolio:
    total_cost += s['shares']*s['price']
    current_value += prices
