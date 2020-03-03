from django.http import JsonResponse
from rest_framework import generics

from locais.filters import LocalizacaoFilter
from locais.models import Localizacao
from locais.serializers import LocalizacaoSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters

from digitalmaps_backend.logger import RequestLogger as rlog
from digitalmaps_backend.logger import Logger as log


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
    def verifica_params_get(request):
        """
        Verifica se os campos de busca são válidos
        TODO criar lista 'campos_validos' automaticamente baseado no dicionario 'fields' em filters.py
        :param request: Request é um objeto de requisição da view. Disponível em qualquer requisição com vários atributos
        :return: True caso os parâmetros de pesquisa estão na lista de "campos_validos", Falso caso contrário
        """
        campos_validos = ['nome__icontains', 'pos_x__exact', 'pos_y__exact', 'hor_abertura__exact',
                          'hor_fechamento__exact']
        params = list(request.GET.keys())
        for param in params:
            if param not in campos_validos:
                rlog.info(request, 'parâmetro ' + param + ' não é um campo válido')
                return False
        rlog.debug(request, 'verificação GET Ok')
        return True

    @staticmethod
    def verifica_fields_post(request, campos_request):
        """
        Verifica se os campos no request POST são válidos para se inserir nova localização
        :param request: Request é um objeto de requisição da view. Disponível em qualquer requisição com vários atributos
        :campos_request: Lista de campos vindos do POST request
        :return: True caso os campos são válidos. False caso contrário.
        """
        campos_validos = ['nome', 'pos_x', 'pos_y', 'hor_abertura', 'hor_fechamento']
        campos_obrigatorios = ['nome', 'pos_x', 'pos_y']
        for campo in campos_request:
            if campo not in campos_validos:
                rlog.info(request, 'Campo ' + str(campo) + ' inválido na verificação de localização via POST')
                return False
        for campo in campos_obrigatorios:
            if campo not in campos_request:
                rlog.info(request, 'Campo ' + str(campo) + ' não enviado pelo POST, e é obrigatório!')
                return False
        if (('hor_abertura' in campos_request and 'hor_fechamento' not in campos_request) and (
                'hor_abertura' not in campos_request and 'hor_fechamento' in campos_request)):
            rlog.info(request, 'Campos hor_abertura ou hor_fechamento descasados')
            return False
        else:
            rlog.debug(request, 'verificação de POST Ok')
            return True  # senão ta tudo certo.

    def get(self, request, *args, **kwargs):
        """
        Override do método GET para incluir a verificação de campos de pesquisa pelo django filters.
        :return: retorna lista vazia caso não passe na verificação. Caso contrário retorna a query serializada de acordo com os parâmetros
        """
        if not self.is_valid_query_params(request):
            rlog.debug(request, 'verificação de GET falhou')
            return JsonResponse({'error': 'request inválido'})
        rlog.debug(request, 'verificação GET Ok')
        return super(LocaisRoot, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Ex:
        {
            "nome": "Casa Mal Assombrada",
            "pos_x": 42,
            "pos_y": 37,
            "hor_abertura": "18:00:00",
            "hor_fechamento": "02:00:00"
        }
        hor_abertura e hor_fechamento opcionais, podem não ser incluídos no corpo do POST.
        :return: - resposta caso a entrada seja válida ou não no banco de dados
        """
        campos_request = list(request.data.keys())
        if not self.verifica_fields_post(request, campos_request):
            rlog.debug(request, 'verificação POST falhou')
            return JsonResponse({'error': 'request inválido'})
        if 'hor_abertura' and 'hor_fechamento' in campos_request:
            Localizacao.objects.create(
                nome=request.data['nome'],
                pos_x=request.data['pos_x'],
                pos_y=request.data['pos_y'],
                hor_abertura=request.data['hor_abertura'],
                hor_fechamento=request.data['hor_fechamento']
            )
            rlog.info(request, 'Localização \'' + request.data['nome'] + '\' criada com horário')
            return JsonResponse({'status': 'Localização \'' + request.data['nome'] + '\' criada com horário'})
        else:
            Localizacao.objects.create(
                nome=request.data['nome'],
                pos_x=request.data['pos_x'],
                pos_y=request.data['pos_y'],
            )
            rlog.info(request, 'Localização \'' + request.data['nome'] + '\' criada sem horário de funcionamento')
            return JsonResponse({'status': 'Localização \'' + request.data['nome'] + '\' criada sem horário de funcionamento'})

    def put(self, request, *args, **kwargs):
        return JsonResponse({}, status=500)

    def delete(self, request, *args, **kwargs):
        return JsonResponse({}, status=500)
