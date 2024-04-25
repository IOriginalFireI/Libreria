from django.db import models
from django.contrib.auth.models import User


class libro(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    año = models.CharField(max_length=10)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img_libros')
    disponible = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Libros"

    def __str__(self):
        return self.titulo
