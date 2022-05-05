#compresión listas
#[x for x in interable (if conditional)]
frutas = ["manzana","kiwi","naranja"]
new = []

for x in frutas:
    if "a" in x:
        new.append(x)
        

new = [x for x in frutas if "a" in x]

new = [x if "a" in x else "" for x in frutas]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
def get_price(price):
    return price if price > 0 else 0

new = [i if i > 0 else 0 for i in original_prices]
new = [get_price(i) for i in original_prices]

print(new)

import time

def bucle_for(n):
    result=[]
    for i in range(n):
        result.append(n**2)
    return result

def listas_com(n):
    return [i**2 for i in range(n)]

# begin = time.time()
# bucle_for(10000000)
# end = time.time()

# print(f"Tiempo ejecución sin comprimir {round(end-begin,2)}")

# begin = time.time()
# listas_com(10000000)
# end = time.time()

# print(f"Tiempo ejecución con compresión {round(end-begin,2)}")


#map()
#map(función, iterable)
 #s[]
def reverse(s):
    return s[::-1]
cadena = "Hola mundo"
print(reverse(cadena))


frutas = ["manzana","kiwi","naranja"]

result = list(map(reverse, frutas))

result = list(map(lambda s : s[::-1], frutas))
print(result)

def f(a, b, c):
    return a + b + c


list(map(f,[1,2],[3,4],[5,6]))
list(map((lambda a, b, c : a + b + c),[1,2],[3,4],[5,6]))

#filter
def is_even(x):
    return x % 2 == 0

list(filter(is_even,range(10)))

list(filter(lambda x :x % 2 == 0 ,range(10)))

def greater_than_100(x):
    return x > 100

list(filter(greater_than_100, [1, 111, 2, 222, 3, 333]))
list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))


#reduce()
#reduce(f, iterable)
from functools import reduce

def f(x, y):
    return x + y

reduce(f, [1, 2, 3, 4, 5])
sum([1, 2, 3, 4, 5])


reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)


print(reduce(f, ["cat", "dog", "hedgehog", "gecko"]))

print("".join(["cat", "dog", "hedgehog", "gecko"]))


import random
import timeit
TAX_RATE = .08
txns = [random.randrange(100) for _ in range(100000)]


def get_price(txn):
    return txn * (1 + TAX_RATE)

def get_prices_with_map():
    return list(map(get_price, txns))

def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]

def get_prices_with_loop():
     prices = []
     for txn in txns:
         prices.append(get_price(txn))
     return prices
 

print(timeit.timeit(get_prices_with_map, number=100))
print(timeit.timeit(get_prices_with_comprehension, number=100))
print(timeit.timeit(get_prices_with_loop, number=100))
