from django.http import JsonResponse
from rest_framework import generics

from locais.filters import LocalizacaoFilter
from locais.models import Localizacao
from locais.serializers import LocalizacaoSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters


class LocaisRoot(generics.ListCreateAPIView):
    """
    View base para retorno genérico de localizacoes utilizando o Django Rest Framework e Django-Filters
    """
    serializer_class = LocalizacaoSerializer
    authentication_classes = []
    queryset = Localizacao.objects.all()
    filter_backends = (filters.DjangoFilterBackend, drf_filters.SearchFilter)
    filterset_class = LocalizacaoFilter
    filterset_fields = ['nome', 'pos_x', 'pos_y', 'hor_abertura', 'hor_fechamento']


    @staticmethod
    def is_valid_query_params(request):
        """
        Verifica se os campos de busca são válidos
        TODO criar lista 'campos_validos' automaticamente baseado no dicionario 'fields' em filters.py
        :param request: Request é um objeto de requisição da view. Disponível em qualquer requisição com vários atributos
        :return: True caso os parâmetros de pesquisa estão na lista de "campos_validos", Falso caso contrário
        """
        campos_validos = ['nome__icontains', 'pos_x__exact', 'pos_y__exact', 'hor_abertura__exact', 'hor_fechamento__exact']
        params = list(request.GET.keys())
        for param in params:
            if param not in campos_validos:
                return False
        return True

    def get(self, request, *args, **kwargs):
        """
        Override do método GET para incluir a verificação de campos de pesquisa pelo django filters.
        :return: retorna lista vazia caso não passe na verificação. Caso contrário retorna a query serializada de acordo com os parâmetros
        """
        if not self.is_valid_query_params(request):
            return JsonResponse({})  # Caso a validação falhe, retorna resposta nula.
        return super(LocaisRoot, self).get(request, *args, **kwargs)
