numeros = [1,2,3,4,5,6]

pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(pares)

#estructuras de la compresión de listas
#[ expresion(i) for i in list if condition ]
#el resultado SIEMPRE sera una lista

pares = [num for num in numeros if num%2 == 0 ] 
print(pares)

cuadrados_ = [num**2 for num in range(10) if num > 5]

cuadrados = [num**2  if num > 5 else 2 for num in range(10) ]
print(cuadrados)

#multuplicacion matrices anidadas
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

matrix = [[1, 2], [3,4], [5,6], [7,8]]

transpose = [[row[i] for row in matrix] for i in range(2)]



#funciones lambda
#lambda parametros : expresión

def cuadrado(x):
    return x**2

cuad = lambda x : x**2

print(cuadrado(2))
print(cuad(2))


#map, filter, reduce

#map()
#map(una_funcion, una_lista)


enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)
     
print(cuadrados)


cuadra = list(map(lambda x : x**2,enteros))

print(cuadra)

#filter()
#filter(una_funcion, una_lista)

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(pares)


pares = list(filter(lambda x: x%2==0,valores))
print(pares)

#reduce()
from functools import reduce

valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el
print(suma)

suma = reduce(lambda x,y:x+y, valores )
print(suma)

print(sum(valores))