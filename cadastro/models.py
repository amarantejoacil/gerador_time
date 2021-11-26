from django.db import models

# Create your models here.

class Jogador(models.Model):
    nome = models.CharField('Nome ou Apelido', max_length=100)
    E_GOLERO = (
        ('N', 'Não'),
        ('S', 'Sim'),
    )
    e_golero = models.BooleanField('É Goleiro??', default=False)

    def __str__(self):
        return self.nome

class Configuracao(models.Model):
    QTD_JOGADOR_LINHA = (
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (8, 8),
        (9, 9),
        (10, 10),
    )
    qtd_jogador_linha = models.IntegerField('Quantidade de jogador no time',
                                            choices=QTD_JOGADOR_LINHA)

    def __str__(self):
        return str(self.qtd_jogador_linha)


