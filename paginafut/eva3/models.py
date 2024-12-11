from django.db import models
from django.contrib.auth.models import User


class Partido(models.Model):
    nombrelocal = models.CharField(max_length=50)
    nombrevisita = models.CharField(max_length=50)
    fecha = models.DateField()
    horapartido = models.TimeField()
    logolocal = models.ImageField(upload_to='logos/', blank=True, null=True)
    logovisita = models.ImageField(upload_to='logos/' , blank=True, null=True)

    def __str__(self):
        return f"{self.nombrelocal} vs {self.nombrevisita}"
    

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, null=True, blank=True)
    texto = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.usuario.username} - {self.partido}"
    

