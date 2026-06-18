class Instrumento:
    def tocar(self):
        print("Som genérico")

class Violao(Instrumento):
    def tocar(self):
        print("♪ Tocando violão ♪")

class Bateria(Instrumento):
    def tocar(self):
        print("Tum Tum Pá!")

class Piano(Instrumento):
    def tocar(self):
        print("♫ Tocando piano ♫")

instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()