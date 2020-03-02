from django_filters import FilterSet

from locais.models import Localizacao


class LocalizacaoFilter(FilterSet):
    """
    Classe do django-filters para ser utilizada com o Django Rest Framework para consultas REST via parâmetros GET.
    Adiciona a extensão "icontains" a "nome", por exemplo. Para poder buscar usando "?nome__icontains=algum_nome"
    """
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


