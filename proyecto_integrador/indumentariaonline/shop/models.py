from django.db import models


class Remera(models.Model):
    marca = models.CharField("Marca", max_length=128)
    TALLES = (
        (1, "XS"),
        (2, "S"),
        (3, "M"),
        (4, "L"),
        (5, "XL"),
        (6, "XXL")
    )
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    color = models.CharField("Color", max_length=128)
    lisa = models.BooleanField("Lisa")
    GENEROS = (
        (1, "Hombre"),
        (2, "Mujer"),
        (3, "Unisex")
    )
    genero = models.PositiveSmallIntegerField("Género", choices=GENEROS)

    def __str__(self):
        return f"{self.marca} {self.color} {self.get_talle_display()}"
