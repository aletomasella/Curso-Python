def es_bisiesto (anio):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False


for año in range(1804, 2022, 4):
    if es_bisiesto(año):
        print(año, "es bisiesto")
    else:
        print(año, "no es bisiesto")

