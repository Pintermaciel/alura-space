from django.db import models

class fotografia(models.Model):

    OPCOES_CATEGORIA = {
        ("NEBULOSA", "nebulosa"),
        ("ESTRELA", "estrela"),
        ("GALÁXIA", "galaxia"),
        ("PLANETA", "planeta"),
    }

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f"Fotografia [nome=quit{self.nome}]"