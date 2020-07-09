#Exercise 1.1
#Python as a calculator
(711.25 - 235.14) * 75

#underscore can be used to hold the result of the last calculation
_ * 0.80

#Exercise 1.2: Getting help

help("for")

# Exercise 1.3: Cutting and Pasting
12 + 20

(3 + 4
         + 5 + 6)

for i in range(5):
    print(i)

#Exercise 1.4: Where is My Bus?
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
from xml.etree.ElementTree import parse
doc = parse(u)
for pt in doc.findall('.//pt'):
    print(pt.text)

# 1.2 A First Program
print('hello world')

for i in range(5):
    print(i)

37 * 42
_ * 2 # the underscore is only true in the interactive mode
_ + 50

#open a text file editor to create hello.py
print('hello world')

#simple if/else construct
if a > b:
    print('Computer says no')
elif a == b:
    print('Computer says yes')
else:
    print('Computer says maybe')

#User input
name = input('Enter your name:')
print('Your name is', name)

#1.3 Numbers
#Four types of numbers: Booleans, Integers, Floating point, complex(imaginary number)
"""
python
a = 37
b = -299392993727716627377128481812241231
c = 0x7fa8      # Hexadecimal
d = 0o253       # Octal
e = 0b10001111  # Binary

x + y      Add
x - y      Subtract
x * y      Multiply
x / y      Divide (produces a float)
x // y     Floor Divide (produces an integer)
x % y      Modulo (remainder)
x ** y     Power
x << n     Bit shift left
x >> n     Bit shift right
x & y      Bit-wise AND
x | y      Bit-wise OR
x ^ y      Bit-wise XOR
~x         Bit-wise NOT
abs(x)     Absolute value

import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)

#Exercise 1.12: A Mystery
int("123")
float("1.23")

# 1.4 Strings

'\n'      Line feed
'\r'      Carriage return
'\t'      Tab
'\''      Literal single quote
'\"'      Literal double quote
'\\'      Literal backslash



a = 'Hello world'
b = a[0]          # 'H'
c = a[4]          # 'o'
d = a[-1]         # 'd' (end of string)


You can also slice or select substrings specifying a range of indices with `:`.

d = a[:5]     # 'Hello'
e = a[6:]     # 'world'
f = a[3:8]    # 'lo wo'
g = a[-5:]    # 'world'
"""
#Concatenation
a = 'Hello' + 'World'
b = 'say' + a

s = '  Hello '
t = s.strip()

s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'

s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'

"""
s.endswith(suffix)     # Check if string ends with suffix
s.find(t)              # First occurrence of t in s
s.index(t)             # First occurrence of t in s
s.isalpha()            # Check if characters are alphabetic
s.isdigit()            # Check if characters are numeric
s.islower()            # Check if characters are lower-case
s.isupper()            # Check if characters are upper-case
s.join(slist)          # Join a list of strings using s as delimiter
s.lower()              # Convert to lower case
s.replace(old,new)     # Replace text
s.rfind(t)             # Search for t from end of string
s.rindex(t)            # Search for t from end of string
s.split([delim])       # Split string into list of substrings
s.startswith(prefix)   # Check if string starts with prefix
s.strip()              # Strip leading/trailing space
s.upper() 
"""

# Exercise 1.13: Extracting individual characters and substrings
symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
symbols[0]
symbols[1]
symbols[2]
symbols[-1]        # Last character
symbols[-2] 

# Exercise 1.14: String concatenation
symbols = symbols + 'GOOG'
symbols

# Exercise 1.15: Membership testing (substring testing)
'IBM' in symbols

'AA' in symbols

'CAT' in symbols

# Exercise 1.16: String Methods
symbols.lower()
symbols.upper()

# Exercise 1.17: f-strings

name = 'IBM'
shares = 100
price = 91.1
f'{shares} shares of {name} at ${price:0.2f}'

# Exercise 1.18: Regular Expressions
# It was not really clear
# To find help on python
s = 'hello'
dir(s) # produces all function that can appear after the '.'

help(s.upper)

# 1.5 Lists
names = [ 'Elwood', 'Jake', 'Curtis' ]
nums = [ 39, 38, 42, 65, 111]

line = 'GOOG,100,490.10'
row = line.split(',')
row

names.append('Anita')
names.insert(2, 'Aretha')

s= [1,2,3]
t=['a', 'b']
s + t

# list are indexed by integers
names = [ 'Elwood', 'Jake', 'Curtis' ]

names[0]
names[1]
names[2]

#negative indices count from the end
names[-1]

#Length of names
len(names)

'Elwood' in names
'Britney' not in names

#Replication (`s * n`).

s = [1, 2, 3]
s * 3  #multiplies the list by 3

for name in names:
    print(name)

names = ['Elwood','Jake','Curtis']
names.index('Curtis') #output is 2

# Using the value
names.remove('Curtis')

# Using the index
del names[1]

# List Sorting -- sort works with any ordered data
s = [10, 1, 7, 3]
s.sort()

# Reverse order
s = [10, 1, 7, 3]
s.sort(reverse=True) 

s = ['foo', 'bar', 'spam']
s.sort()

#Use `sorted()` if you'd like to make a new list instead:

t = sorted(s)

# Exercise 1.19: Extracting and reassigning list elements
symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')
symlist[0]
symlist[1]
symlist[-1]
symlist[-2]

#Reassigning one value: (add to a list**)
symlist[2] = 'AIG'

#Slice
symlist[0:3] # the first 3
symlist[-2:] # last two on the list

# Exercise 1.20: Looping over list items
for s in symlist:
    print('s =', s)

#Exercise 1.21: Membership tests
'AIG' in symlist
'AA' in symlist
'CAT' not in symlist

# Exercise 1.22: Appending, inserting, and deleting items
symlist[-1] = 'RHT'
symlist.insert(1, 'AA')
symlist.remove('MSFT')
symlist.append('YHOO')
symlist[4]
symlist.count('YHOO')

#to remove duplicates from the list
symlist = list(dict.fromkeys(symlist))
print(symlist)

# Exercise 1.24: Putting it all back together
# Want to take a list of strings and join them together into one string?
# Use the `join()`
a = ','.join(symlist)
b = ':'.join(symlist)
c = ''.join(symlist)

# Exercise 1.25: Lists of anything 
# Nested Lists
nums = [101, 102, 103]
items = ['spam', symlist, nums]
items

# 1.6 File Management
# File Input and Output
f = open('foo.txt', 'rt')     # Open for reading (text)
g = open('bar.txt', 'wt')     # Open for writing (text)

# Read data
data = f.read()

# Read only up to 'maxbytes' bytes
data = f.read([maxbytes])

# Close when you are done
f.close()
g.close()

with open(filename, 'rt') as file:
    # Use the file `file`
    ...
    # No need to close explicitly
    #It automatically closes when control leaves the indented code block

with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` is a string with all the text in `foo.txt`

Read a file line-by-line by iterating.

with open(filename, 'rt') as file:
    for line in file:
        # Process the line

with open('outfile', 'wt') as out:
    out.write('Hello World\n')

#Redirect the print file
with open('outfile', 'wt') as out:
    print('Hello World', file=out)

# Exercise 1.26: File Preliminaries
import os
os.getcwd()
with open('Data/portfolio.csv', 'rt') as f:
    data = 'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
    print(data)

 with open('Data/portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
headers

for line in f:
    print(line, end='')

"""
`next()` returns the next line of text in the file. If you were to call it repeatedly, you would get successive lines.
However, just so you know, the `for` loop already uses `next()` to obtain its data.
"""
#Once you’re reading lines of a file, you can start to perform more processing such as splitting.
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
headers
for line in f:
    row = line.split(',')
    print(row)
f.close() # f.close() was called because the with statement isn't used

# Exercise 1.28: Other kinds of "files"
# Python has a library module `gzip` that can read gzip compressed files.
import gzip
with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

