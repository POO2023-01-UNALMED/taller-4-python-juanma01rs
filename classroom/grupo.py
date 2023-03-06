from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo = "grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, lista2=None, **kwargs):
        for key in kwargs():
            if lista2 == None:
                lista2 = []
            lista2.append(kwargs[key])
            if self._asignaturas == None:
                self._asignaturas = lista2
            else:
                self._asignaturas = self._asignaturas + lista2

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
        lista.append(alumno)
        if self.listadoAlumnos == None:
            self.listadoAlumnos = lista
        else:
            self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena 
    
    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 10"):
    #     cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre
