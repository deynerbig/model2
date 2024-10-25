from django.db import models
class caballo (models.Model):
    nivel=[
        ('alta','alta'),
        ('media','media'),
        ('baja','baja'),
    ]
    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    color=models.CharField(max_length=20)
    velocidad= models.CharField(max_length=5,choices=nivel) 
    resistencia= models.CharField(max_length=5,choices=nivel)
# Create your models here.
