import django_filters

from locais.models import Localizacao


class LocalizacaoFilter(django_filters.FilterSet):
    class Meta:
        model = Localizacao
        fields = {
            'nome': ['icontains'],
            'pos_x': ['exact'],
            'pos_y': ['exact'],
            'hor_abertura': ['exact'],
            'hor_fechamento': ['exact']
        }


