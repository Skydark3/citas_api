from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reservas_usuario'
  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'reservas_cita'
     

    def __str__(self):
        return f"Cita {self.id} - {self.fecha}"
