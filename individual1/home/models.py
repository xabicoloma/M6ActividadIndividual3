from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Usuario(User):
    nombre = models.CharField(max_length=50,  null=True)
    apellido = models.CharField(max_length=50,  null=True)
    rut = models.CharField(max_length=50,  null=True)
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateTimeField(auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)