from rest_framework import serializers
from .models import *


class LocalizacaoSerializer(serializers.ModelSerializer):
    """
    Utilizado pelo django rest framework para serializar dados dos models (tabelas)
    Exclui da serialização dados do banco de dados sensíveis, como quem cadastrou, id, datas de criação e modificação, etc...
    Pode ser passado o unique_id caso necessário.
    """
    class Meta:
        model = Localizacao
        fields = ['nome', 'pos_x', 'pos_y', 'hor_abertura', 'hor_fechamento']
        # exclude = ('id', 'unique_id', 'created', 'modified', 'user')
