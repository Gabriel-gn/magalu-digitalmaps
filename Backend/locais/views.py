from django.http import JsonResponse
from rest_framework import generics

from locais.filters import LocalizacaoFilter
from locais.models import Localizacao
from locais.serializers import LocalizacaoSerializer
from django_filters import rest_framework as filters


class LocaisRoot(generics.ListCreateAPIView):
    serializer_class = LocalizacaoSerializer
    authentication_classes = []
    queryset = Localizacao.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LocalizacaoFilter
    filterset_fields = ['nome', 'pos_x', 'pos_y', 'hor_abertura', 'hor_fechamento']
