from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    semestre = models.IntegerField()
    creditos = models.IntegerField()

    def _str_(self):
        return f'{self.nombre} - (${self.creditos})'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def _str_(self):
        return f'{self.nombre} <{self.correo}>'
    
class Programa(models.Model):
    nombre = models.CharField(max_length=120)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='programa')
    curso = models.ManyToManyField(Curso, related_name='programa')

    def _str_(self):
        return f'Programa #{self.pk} - {self.estudiante.nombre}'