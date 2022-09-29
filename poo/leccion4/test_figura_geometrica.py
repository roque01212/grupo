from Cuadrado import Cuadrado
from Rectangulo import Rectangulo



print('Creación Objeto Cuadrado'.center(50,"-"))
cuadrado1=Cuadrado(9, 'Red')
print(f"Cálculo área cuadrado: {cuadrado1.area()}")
print(cuadrado1)

print('Creación Objeto Rectangulo'.center(50,"-"))
rectangulo1=Rectangulo(9,2,"Blue")
print(f"Cálculo área Rectángulo: {rectangulo1.area()}")
rectangulo1.ancho=50
print(rectangulo1)