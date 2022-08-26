class Alumno:
  def __init__(self, nombre, nota):
    self.nombre = nombre if nombre else "NN"
    self.nota = nota if nota else 0

  def isAproved(self):
    if self.nota >= 6:
      return f"El alumno {self.nombre} está aprobado con una nota de {self.nota}"
    else:
      return f"El alumno {self.nombre} no está aprobado, su calificacion es de {self.nota}"


  def setNote(self, nota):
    self.nota = nota if nota else 0

  def setName(self, nombre):
    self.nombre = nombre if nombre else "NN"


alumno1 = Alumno("Juan", 7)
alumno2 = Alumno("Pedro", 5)
alumno3 = Alumno("Ana", 8)

print(alumno1.isAproved())
print(alumno2.isAproved())
print(alumno3.isAproved())