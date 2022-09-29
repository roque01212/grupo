class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs) -> None:
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad
        # self.args=args
        # self.kwargs=kwargs

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
    
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido=apellido
    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad=edad

    def mostrar_detalle(self):
        return f"{self._nombre} {self._apellido} {self._edad} "

    """Eliminacion del objeto"""
    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido}")
# persona1=Persona('roque', 'gerez', 32, 11, 'estela', True, color='red', dato='1122', telefono=123321)

if __name__=='__main__':
    persona1=Persona('roque', 'gerez', 32)

    print(persona1.mostrar_detalle())
    print(__name__) # al ejecutarlo deesde otro archivo ya no devuelve __main__