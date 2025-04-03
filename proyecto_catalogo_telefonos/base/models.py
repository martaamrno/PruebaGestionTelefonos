from django.db import models

# Create your models here.
class Telefonos(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del dispositivo")
    fabricante = models.CharField(max_length=50, unique=True, verbose_name="Nombre del fabricante")
    fecha_lanzamiento = models.DateField(verbose_name= "fecha de lanzamiento")
    precio = models.IntegerField(verbose_name="Precio ")
    sistemaOperativo = models.CharField(max_length=100, unique=True, verbose_name="Sistema Operativo del dispositivo")
    disponibilidad = models.BooleanField(verbose_name= "disponibilidad")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Última modificación")

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre + "("+ self.fabricante+")"