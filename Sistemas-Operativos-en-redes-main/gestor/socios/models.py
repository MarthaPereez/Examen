from django.db import models

# Create your models here.
class socio (models.Model):
    id = models.AutoField(primary_key=True)
    numero_socio  = models.CharField(max_length=15, blank= False)
    contraseña = models.CharField(max_length=20, blank= False)
    DNI = models.CharField(max_length=20, blank= False)