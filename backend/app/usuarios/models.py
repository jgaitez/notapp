
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(
        primary_key=True
        )

    username = models.CharField(
        db_column='username',
        max_length=50
        )

    nombre = models.CharField(
        db_column='nombre',
        max_length=50
        )

    apellido = models.CharField(
        db_column='apellido',
        max_length=50
        )

    mail = models.CharField(
        db_column='correo',
        max_length=50
        )

    def __str__(self):
        texto = '({0}) {1} {2}'
        return texto.format(self.id_usuario, self.nombre, self.apellido)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'