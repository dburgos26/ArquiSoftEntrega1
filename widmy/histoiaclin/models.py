from django.db import models

# Create your models here.

class HistoiaClin(models.Model):
    nombrePaciente = models.CharField(max_length=50)
    apellidoPaciente = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1)
    documento = models.CharField(max_length=10)

    def __str__(self):
        return '{}' .format(self.documento)