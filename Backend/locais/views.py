from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics

from locais.filters import LocalizacaoFilter
from locais.models import Localizacao
from locais.serializers import LocalizacaoSerializer
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters
from django.forms.models import model_to_dict
from django.core import serializers
import json
import math
import datetime

from digitalmaps_backend.logger import RequestLogger as rlog
from digitalmaps_backend.logger import Logger as log
from locais.tasks import horario_no_intervalo


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
        ex: localhost:8000/locais/?nome__icontains=casa
        :return: retorna lista vazia caso não passe na verificação. Caso contrário retorna a query serializada de acordo com os parâmetros
        """
        if not self.verifica_params_get(request):
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


class LocaisUser(generics.ListCreateAPIView):
    """
    View base para retorno específico das requisições de localizacoes requisitadas pela vaga.
    """
    serializer_class = LocalizacaoSerializer
    authentication_classes = []
    queryset = Localizacao.objects.all()

    @staticmethod
    def verifica_params_get(request, params):
        """
        Verifica se os campos de busca são válidos para a requisição do pdf da vaga
        TODO validar typeof/InstanceOf das entradas. Ex: pos_x deve ser um número inteiro positivo, etc...
        :param request: Request é um objeto de requisição da view. Disponível em qualquer requisição com vários atributos
        :return: True caso os parâmetros de pesquisa estão na lista de "campos_validos", Falso caso contrário
        """
        campos_validos = ['pos_x', 'pos_y', 'mts', 'hr']
        campos_obrigatorios = ['pos_x', 'pos_y', 'mts', 'hr']
        msg = 'verificação GET Ok'
        for param in params:
            if param not in campos_validos:
                msg = 'parâmetro \'' + param + '\' não é um campo válido'
                rlog.info(request, msg)
                return False
        for param in campos_obrigatorios:
            if param not in params:
                msg = 'parâmetro \'' + param + '\' é obrigatório e não foi fornecido'
                rlog.info(request, msg)
                return False
        rlog.debug(request, msg)
        return True

    def get(self, request, *args, **kwargs):
        """
        ex: localhost:8000/locais/user?pos_x=10&pos_y=10&mts=10&hr=10:00:00
        Valida params get, busca no banco de dados objetos com distancias até a maxima ou mínima, ajusta e retorna resultados.
        :return:
        """
        params = list(request.GET.keys())
        if not self.verifica_params_get(request, params):
            rlog.debug(request, 'verificação de GET falhou')
            return JsonResponse({'error': 'request inválido'})
        rlog.debug(request, 'verificação GET Ok')

        # valores que vieram dos params do GET
        pos_x = int(request.GET['pos_x'])
        pos_y = int(request.GET['pos_y'])
        mts = int(request.GET['mts'])
        hr = str(request.GET['hr']).split(':')
        hr = datetime.time(int(hr[0]), int(hr[1]), int(hr[2]))

        # verificação de distância
        x_min = (pos_x - mts) if (pos_x - mts) >= 0 else 0
        x_max = pos_x + mts
        y_min = (pos_y - mts) if (pos_y - mts) >= 0 else 0
        y_max = pos_y + mts
        locais = Localizacao.objects.filter(Q(Q(pos_x__gte=x_min) & Q(pos_x__lte=x_max) & Q(pos_y__gte=y_min) & Q(pos_y__lte=y_max)))

        # validações finais antes de entregar o resultado bonito pro frontend
        locais_finais = list()
        for local in locais:
            local_json = json.loads(serializers.serialize('json', [ local, ]))[0]['fields']
            distancia = math.sqrt((local_json['pos_x'] - pos_x) ** 2 + (local_json['pos_y'] - pos_y) ** 2)
            local_json['distancia'] = float(distancia)
            local_json['no_perimetro'] = True if distancia <= mts else False  # isso pode ser condição de incluir ou não na lista

            if local_json['hor_abertura']:
                hor_abertura = str(local_json['hor_abertura']).split(':')
                hor_abertura = datetime.time(int(hor_abertura[0]), int(hor_abertura[1]), int(hor_abertura[2]))
                hor_fechamento = str(local_json['hor_fechamento']).split(':')
                hor_fechamento = datetime.time(int(hor_fechamento[0]), int(hor_fechamento[1]), int(hor_fechamento[2]))
                local_json['opened'] = True if (horario_no_intervalo(hor_abertura, hor_fechamento, hr)) else False
            else:
                local_json['opened'] = True
            if local_json['no_perimetro']:
                locais_finais.append(local_json)

        return JsonResponse(locais_finais, safe=False)

    def post(self, request, *args, **kwargs):
        return JsonResponse({}, status=500)

    def put(self, request, *args, **kwargs):
        return JsonResponse({}, status=500)

    def delete(self, request, *args, **kwargs):
        return JsonResponse({}, status=500)