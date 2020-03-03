from django.conf import settings
from django.db import models
from django_extensions.db.fields import ShortUUIDField


class Default(models.Model):
    """
    Model com campos padrão que serão herdados por todos os modelos subsequentes.
    O campo 'id' é a primary key por padrão dos modelos criados no banco de dados.
    O campo 'unique_id' é criado apenas por fins de não referenciar o id da linha diretamente caso necessário.
    """
    unique_id = ShortUUIDField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created']


class Localizacao(Default):
    """
    Herda modelo padrão.
    Tabela com propósito de gravar localizações com ponto de localização (pos_x, pos_y) e horário de funcionamento.
    """
    nome = models.TextField(default='Sem identificação', null=True, blank=True)
    pos_x = models.PositiveIntegerField()
    pos_y = models.PositiveIntegerField()
    hor_abertura = models.TimeField(null=True, blank=True)
    hor_fechamento = models.TimeField(null=True, blank=True)

    def __str__(self):
        return str(self.nome)
