from mimetypes import init


class Cubo:
    
    def __init__(self, ancho, alto, profundo) -> None:
        self.ancho=ancho
        self.alto=alto
        self.profundo=profundo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo

ancho=int(input('Proporcine el ancho: '))
alto=int(input('Proporcine el alto: '))
profundo=int(input('Proporcine lo profundo: '))


cubo1=Cubo(ancho, alto, profundo)
print(f"Volúmen cubo {cubo1.calcular_volumen()}")