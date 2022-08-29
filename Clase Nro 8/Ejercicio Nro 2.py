import pickle
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca if marca else "Marca Mongo"
        self.modelo = modelo if modelo else "Modelo Mongo"
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


auto = Vehiculo("Ferrari", "FT71")
f = open("datos.bin", "wb")
pickle.dump(auto, f)
f.close()


f = open("datos.bin", "rb")
auto = pickle.load(f)
f.close()

print(auto.estado())


