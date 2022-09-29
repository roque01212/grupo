class MiClase:

    variable_clase='Variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia=variable_instancia

    
    """METODO ESTATICO SE ASOCIA CON LA CLASE MISMA"""
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase) 
        """No puede acceder a la variable de instancia solo a 
        las de clases"""

    """METODO DE CLASE SI RECIBE contexto DE LA CLASE CLS 
    hace referencia a la clase misma"""
    @classmethod
    def metodo_clase(cls):
        """con cls podemos acceder la variable de clase sin usar 
        el nombre de clase"""
        print(cls.variable_clase)
MiClase.metodo_estatico()
MiClase.metodo_clase()

# print(MiClase.variable_clase)
# miClase=MiClase('valor variable instancia')
# print(miClase.variable_instancia)
# print(miClase.variable_clase)

# """CREACION DE VARIABLE DE CLASE AL VUELO"""
# MiClase.variable_clase2='Valor variable clase 2'

# miClase2=MiClase('Otro valor de instacia')
# print(miClase2.variable_instancia)
# print(miClase2.variable_clase)
# print(miClase2.variable_clase2)