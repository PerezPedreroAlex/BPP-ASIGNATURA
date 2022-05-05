def is_even(x):
  return x % 2 != 0

primos = list(filter(is_even,[3, 4, 8, 5, 5, 22, 13]))

print(primos)