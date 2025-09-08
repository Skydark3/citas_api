from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="citas")
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.usuario.nombre} el {self.fecha} a las {self.hora}"


