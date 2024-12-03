from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):  # Nombre en PascalCase
    nombre = models.CharField(max_length=100)  # Ajusté max_length a 100 según el enunciado
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Cambié FloatField por DecimalField
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Correcto para registrar la fecha automáticamente
    stock = models.IntegerField(default=0)  # Nuevo campo

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"