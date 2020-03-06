from model_bakery import baker
from django.test import TestCase
from locais.models import Localizacao, Default

from django.db import models
from django_extensions.db.fields import ShortUUIDField


class TestsModelsLocalizacao(TestCase):

    def setUp(self):
        """
        Cria o necessário para rodar os testes desta classe
        """
        self.nova_localizacao = baker.make('locais.Localizacao')
        self.campos_modelo = self.nova_localizacao._meta.fields

    def test_criacao_localizacao(self):
        """
        Verifica se o modelo é uma instância dele mesmo
        Verifica se o retorno __str__ é o nome da localização
        """
        self.assertTrue(isinstance(self.nova_localizacao, Localizacao))
        self.assertEqual(self.nova_localizacao.__str__(), self.nova_localizacao.nome)

    def test_verificar_campos(self):
        """
        Verifica se os campos em 'lista_campos_teste' são iguais aos esperados no modelo Localização
        """
        lista_campos_teste = ['id', 'unique_id', 'created', 'modified', 'nome', 'pos_x', 'pos_y', 'hor_abertura', 'hor_fechamento']
        lista_campos_modelo = list(map(lambda x: x.attname, self.campos_modelo))
        self.assertCountEqual(lista_campos_teste, lista_campos_modelo)  # lista de mesmo tamanho
        self.assertEqual(lista_campos_teste, lista_campos_modelo)
        for campo in lista_campos_modelo:  # o que existe no modelo está no que é esperado?
            self.assertIn(campo, lista_campos_teste)
        for campo in lista_campos_teste:  # o que é esperado está no modelo?
            self.assertIn(campo, lista_campos_modelo)


    def test_verificar_instância_campos(self):
        """
        Verifica se os modelos de campos são instâncias do que é esperado
        """
        instance_dict = {
            'id': models.fields.AutoField,
            'unique_id': ShortUUIDField,
            'created': models.DateTimeField,
            'modified': models.DateTimeField,
            'nome': models.TextField,
            'pos_x': models.PositiveIntegerField,
            'pos_y': models.PositiveIntegerField,
            'hor_abertura': models.TimeField,
            'hor_fechamento': models.TimeField
        }
        for campo in self.campos_modelo:
            self.assertIsInstance(campo, instance_dict[campo.name])



