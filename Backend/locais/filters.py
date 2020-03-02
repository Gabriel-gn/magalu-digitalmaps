from django_filters import FilterSet

from locais.models import Localizacao


class LocalizacaoFilter(FilterSet):
    strict = True

    class Meta:
        model = Localizacao
        fields = {
            'nome': ['icontains'],
            'pos_x': ['exact'],
            'pos_y': ['exact'],
            'hor_abertura': ['exact'],
            'hor_fechamento': ['exact']
        }


