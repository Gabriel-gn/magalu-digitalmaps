from django.test import TestCase
import json

from model_bakery import baker


class TestCalls(TestCase):

    def setUp(self):
        """
        Cria o necessário para rodar os testes desta classe
        """
        self.nova_localizacao = baker.make('locais.Localizacao')
        self.campos_modelo = self.nova_localizacao._meta.fields

    def test_get_hello_world(self):
        """
        Testa a landing page com uma mensagem amigável :)
        """
        response = self.client.get('/', follow=True)
        self.assertEqual(response.content.decode(), '{"Hello": "World", "Ol\\u00e1": "Galera do labs"}')


    def test_verifica_locais_get(self):
        """
        Verifica se os campos recebidos no json condizem com os do modelo
        """
        lista_campos_modelo = list(map(lambda x: x.attname, self.campos_modelo))
        response = self.client.get('/locais/?nome__icontains=', follow=True)
        json_response = json.loads(response.content.decode())[0]
        chaves_json = list(json_response.keys())
        self.assertCountEqual(lista_campos_modelo, chaves_json)  # lista de mesmo tamanho
        self.assertEqual(lista_campos_modelo, chaves_json)


    def test_verifica_locais_post(self):
        """
        Verifica se um POST comum é aceito pela view de adição de locais
        """
        dados = {
                    "nome": "Casa Mal Assombrada 2",
                    "pos_x": 18,
                    "pos_y": 88,
                    "hor_abertura": "19:00:00",
                    "hor_fechamento": "03:00:00"
                }
        response = self.client.post(path='/locais/?nome__icontains=', data=dados, content_type='application/json', follow=True)
        json_response = json.loads(response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['status'], 'ok')


    def test_verifica_locais_usuario_get(self):
        """
        Verifica o retorno por input do usuário com dados pos_x(int>=0), pos_y(int>=0), mts(int>=0) e hr(format hh:mm:ss)
        """
        response = self.client.get('/locais/user?pos_x=10&pos_y=10&mts=10&hr=10:00:00', follow=True)
        json_response = json.loads(response.content.decode())[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response['status'], 'ok')