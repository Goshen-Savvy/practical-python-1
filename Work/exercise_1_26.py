import os
os.getcwd()
with open('Data/portfolio.csv', 'rt') as f:
    data = 'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
    print(data)

f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
headers
for line in f:
    row = line.split(',')
    print(row)