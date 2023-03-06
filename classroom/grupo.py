from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = ('Grupo de estudiantes: ' + grupo)
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for key in kwargs.values():
            if key not in self._asignaturas:
                self._asignaturas.append(Asignatura[key])

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
        lista.append(alumno)
        if self.listadoAlumnos == None:
            self.listadoAlumnos = lista
        else:
            self.listadoAlumnos = self.listadoAlumnos + lista

    # def __str__(self):
    #     pass

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 10"):
    #     cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    # @ classmethod
    # def asignarNombre(cls, nombre="Grado 4"):
    #     cls.grado = nombre
