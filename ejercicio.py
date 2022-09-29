class Alumno:
    id_alumno=0

    @classmethod
    def incrementar_id(cls):
        cls.id_alumno+=1
        return cls.id_alumno


    def __init__(self, nombre, apellido, edad) -> None:
        self.id_alumno=Alumno.incrementar_id()
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def __str__(self):
        return f"""
        ID: {self.id_alumno}
        Nombre Completo: {self.nombre} {self.apellido}
        """

class Servicio:
    id_servicio=0

    @classmethod
    def incrementar_id(cls):
        cls.id_servicio+=1
        return cls.id_servicio

    def __init__(self, nombre, monto, alumnos):
        self.id_servicio=Servicio.incrementar_id()
        self.nombre=nombre
        self.monto=monto
        self.alumnos=list(alumnos)

    def agregar_alumnos(self, alumno):
        self.alumnos.append(alumno)
        return self.alumnos

    def __str__(self):
        str_alumno=""
        for alumno in self.alumnos:
            str_alumno += alumno.__str__()

        return f"""
            ID:{self.id_servicio}
            Nombre Servicio: {self.nombre}
            Precio Servicio: {self.monto}
        Alumnos Inscriptos:{str_alumno}
        """


    

alumno1=Alumno('Roque', 'gerez', 32)
alumno2=Alumno('Emanuel', 'gerez', 20)
alumno3=Alumno('Carmen', 'Ferreira', 40)

alumnos=(alumno1, alumno2)

servicio1=Servicio('luz', 2000, alumnos)
servicio1.agregar_alumnos(alumno3)
print(servicio1)