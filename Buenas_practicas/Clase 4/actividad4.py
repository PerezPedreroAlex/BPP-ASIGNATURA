# import pdb
# pdb.set_trace()

numeros = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

maximos = []

for lista in numeros:
    maximos.append(max(lista))

print(maximos)

###########################################################


def is_even(x):
  return x % 2 != 0

primos = list(filter(is_even,[3, 4, 8, 5, 5, 22, 13]))
primos2 = list(filter(lambda x: x%2 != 0,[3, 4, 8, 5, 5, 22, 13]))

print(primos)
print(primos2)



     
