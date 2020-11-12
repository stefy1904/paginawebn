from django.db import models

# Create your models here.
class Usuario (models.Model):
    Pnombre = models.CharField(max_length = 30)
    Apellido = models.CharField(max_length = 30)
    Email = models.CharField(max_length = 100)
    Telefono = models.CharField(max_length = 12)
    Mensaje = models.CharField(max_length = 10000)
    
