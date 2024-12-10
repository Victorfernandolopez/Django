from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField("nombre",max_length=128)
    inscriptos = models.IntegerField("inscriptos")
    TURNOS=(
        (1,'Mañana'),
        (2,'Tarde'),
        (3,'Noche')
    )
    turno = models.PositiveSmallIntegerField("turno",choices=TURNOS)
    Profesor = models.ForeignKey(Profesor,on_delete=models.SET_NULL,null=True,related_name='cursos')

    def __str__(self):
        return self.nombre

class Adidas(models.Model):
    articulo = models.CharField("articulo",max_length=128)
    talle = models.CharField("talle",max_length=128)