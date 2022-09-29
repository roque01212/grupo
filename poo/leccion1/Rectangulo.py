class Rectangulo:
    def __init__(self, base, altura):
        self.altura=altura
        self.base=base

    def calcular_area(self):
        area=self.base*self.altura

        return area
base=int(input('Proporciona la base: '))
altura=int(input('Proporciona la altura: '))

rectangulo1=Rectangulo(base, altura)

print(f'Área Rectangulo: {rectangulo1.calcular_area()}')