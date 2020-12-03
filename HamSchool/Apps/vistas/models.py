from django.db import models

# Create your models here.


class Curso (models.Model):
    clase = models.CharField(max_length=50)
    Grado = models.CharField(max_length=35)

    def Curso (self):
        cadena = "{0}, {1}"
        return cadena.format( self.Grado, self.clase)

    def __str__(self):
        return self.Curso()


class Usuario (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)

    tipo = (('Maestro', 'Maestro'), ('Alumno', 'Alumno'))
    Tipo = models.CharField(max_length=7, choices=tipo, default='Alumno')

    correo = models.CharField(max_length=50)


    def Nombrecompleto(self):
        cadena = "{0} {1} {2} "
        return cadena.format(self.Tipo,self.nombres, self.apellidos)

    def __str__(self):
        return self.Nombrecompleto()
