from django.db import models
from django.core.validators import RegexValidator

class Alumno(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre completo"
    )
    
    email = models.EmailField(
        unique=True,
        verbose_name="Correo electrónico"
    )
    
    telefono = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Número de teléfono debe tener entre 9-15 dígitos"
        )],
        verbose_name="Teléfono"
    )
    
    fecha_nacimiento = models.DateField(
        verbose_name="Fecha de nacimiento"
    )
    
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de registro"
    )
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ['-fecha_registro']