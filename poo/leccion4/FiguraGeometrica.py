
""" ABC = Abstract Base Class"""
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
            if self._validar_valor(ancho):
                self._ancho=ancho
            else:
                self._ancho=0
                print(f"valor erroneo ancho: {self._ancho}")
            if self._validar_valor(alto):    
                self._alto=alto
            else:
                self._alto=0
                print(f"valor erroneo alto: {self._alto}")
    
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
                self._ancho=ancho
        else:
            self._ancho=0
            print(f"valor erroneo ancho: {self._ancho}")
        

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):    
                self._alto=alto
        else:
            self._alto=0
            print(f"valor erroneo alto: {self._alto}")
    
    

    """
    -AL CREAR UN METODO ABSTRACTO OBLIGAMOS A LOS 
        OBJETOS QUE EREDAN DE ELLA A QUE LO IMPLEMENTEN SI O SI
    - TAMBIEN AL CREAR UN METODO ABSTRACTO TODA LA CLASE
        SE VUELVE ABSTRACTA LO QUE SIGNIFICA QUE NO SE PUEDEN 
        CREAR INSTACIAS DE ELLA
    """
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]"

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False