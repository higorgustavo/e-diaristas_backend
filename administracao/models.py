from django.db import models


class Servico(models.Model):
    ICONE_CHOICES = (
        ('twf-cleaning-1', 'twf-cleaning-1'),
        ('twf-cleaning-2', 'twf-cleaning-2'),
        ('twf-cleaning-3', 'twf-cleaning-3'),
    )
    nome = models.CharField(max_length=50)
    valor_minimo = models.DecimalField(decimal_places=2, max_digits=5)
    qtd_horas = models.IntegerField()
    porcentagem_comissao = models.DecimalField(decimal_places=2, max_digits=5)
    horas_quarto = models.IntegerField()
    valor_quarto = models.DecimalField(decimal_places=2, max_digits=5)
    horas_sala = models.IntegerField()
    valor_sala = models.DecimalField(decimal_places=2, max_digits=5)
    horas_banheiro = models.IntegerField()
    valor_banheiro = models.DecimalField(decimal_places=2, max_digits=5)
    horas_cozinha = models.IntegerField()
    valor_cozinha = models.DecimalField(decimal_places=2, max_digits=5)
    horas_quintal = models.IntegerField()
    valor_quintal = models.DecimalField(decimal_places=2, max_digits=5)
    horas_outros = models.IntegerField()
    valor_outros = models.DecimalField(decimal_places=2, max_digits=5)
    icone = models.CharField(choices=ICONE_CHOICES, max_length=14)
    posicao = models.IntegerField(null=False)
