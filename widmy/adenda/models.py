from django.db import models
from histoiaclin.models import HistoiaClin

# Create your models here.

class Adenda(models.Model):
    historia = models.ForeignKey(HistoiaClin, on_delete=models.CASCADE)
    fecha = models.DateField()
    identificacion = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return '{}' .format(self.identificacion)