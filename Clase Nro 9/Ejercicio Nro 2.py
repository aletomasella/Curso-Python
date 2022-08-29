from functools import reduce


lista = [1,2,3,45,5,6,7,7,8,89,765,5,4,3,2,1]

notEvenNumbers = list(filter(lambda x: x % 2 != 0, lista))
print(notEvenNumbers)

total = reduce(lambda x, y: x + y, notEvenNumbers)
print(total)