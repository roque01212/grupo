from Persona import Persona


print('Creacion Persona Prueba'.center(50, '-'))
persona1=Persona('roque', 'gerez', 32)
print(persona1.mostrar_detalle())

print('Eliminacion de objeto'.center(50,'-'))

"""LLama al metodo de la clase para eliminar el objeto creado"""
del persona1