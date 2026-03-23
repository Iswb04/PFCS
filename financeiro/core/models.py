from django.db import models

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('R', 'Receita'),
        ('D', 'Despesa'),
    ]

    titulo = models.CharField(max_length=100)
    valor = models.FloatField()
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo