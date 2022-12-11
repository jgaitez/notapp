from django.db import models
from app.usuarios.models import Usuario

class Nota(models.Model):

    estados_nota_opciones = (
        ('1', 'Pendiente'),
        ('2', 'En curso'),
        ('3', 'Cerrado')
    )

    id_nota = models.AutoField(
        primary_key=True
        )

    titulo = models.CharField(
        max_length=100
        )

    cuerpo = models.TextField(

    )

    # id_usuario = models.ForeignKey(
    #     'Usuario',
    #     models.DO_NOTHING,
    #     db_column='id_usuario'
    #     )

    estado = models.CharField(
        max_length=1,
        choices=estados_nota_opciones,
    )


    def __str__(self):
        texto = '({0}) {1}'
        return texto.format(self.id_nota, self.titulo)
    class Meta:
            verbose_name = 'nota'
            verbose_name_plural = 'notas'
            db_table = 'notas'
            