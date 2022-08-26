class Vehiculo:
  def __init__(self,color,ruedas,puertas):
    self.color = color if color else "Blanco"
    self.ruedas = ruedas if ruedas else 4
    self.puertas = puertas if puertas else 4


class Coche(Vehiculo):
  def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
    super().__init__(color, ruedas, puertas)
    self.velocidad = velocidad if velocidad else 100
    self.cilindrada = cilindrada if cilindrada else 1000


coche = Coche(puertas=2, color="Rojo", ruedas=4, velocidad=200, cilindrada=1200)

print(coche.puertas)
print(type(coche))
