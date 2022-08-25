print("Ingresa tu peso en KG y estatura en metros")
x = input("Peso: ")
y = input("Estatura: ")

print("Tu IMC es: " + str(round(float(x)/(float(y)*float(y)),2)))
