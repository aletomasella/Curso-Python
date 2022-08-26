def esPrimo (numero):
    if numero == 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, numero, 2):
        if numero % i == 0:
            return False
    return True

print(esPrimo(1))
print(esPrimo(2))
print(esPrimo(3))
print(esPrimo(4))
print(esPrimo(5))
print(esPrimo(11))
print(esPrimo(13))
print(esPrimo(23))
print(esPrimo(50))
print(esPrimo(79))