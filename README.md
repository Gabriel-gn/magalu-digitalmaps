# Magalu Digital Maps

Este projeto tem por finalidade criar e consumir uma API REST na qual é possível cadastrar localizações com nome, posição x, posição y e horário de funcionamento (abertura e fechamento, opcionais).

# Configurando Backend em Django

### Requisitos:
  - Python >= versão 3.6
  - PostgreSQL >= versão 10

### Como preparar o projeto:
#### Postgres:

Criar uma base postgres. Em seguida alterar, dentro do arquivo `Backend/digitalmaps_backend/settings.py`, as chaves do dicionário "DATABASES" de acordo com a necessidade:
- **NAME**: nome da database em postgres (padrão: 'digitalmaps')
- **USER**: nome do usuário dono da base (padrão: 'postgres')
- **PASSWORD**: senha do usuário dono da base (padrão: 'magalu')
- **HOST**:  URL do local da base (padrão: 'localhost')
- **PORT**:  porta alocada para acessar a database no host (padrão: '5432')

Lembrando que é possível iniciar uma base postgres já com as configurações padrões via docker seguindo as instruções do arquivo `Backend/postgres/leiame.md`

#### Python/Django:

Instalar python versão igual ou superior a 3.6.
Verificar instalação do Pip, utilizando o comando `python3 -m pip --version`. 
Caso o pip não esteja instalado, instalar usando: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` e após, `python3 get-pip.py`

Navegue até o diretório `Backend` e instale as dependências do projeto utilizando `python3 -m pip install -r requirements.txt`.
Verifique se as dependências foram corretamente instaladas com `python3 -m pip freeze`. Caso os mesmos nomes do arquivo requirements.txt estejam na saída do comando executado acima, está tudo certo.

Ainda na pasta `Backend`, execute `python3 manage.py migrate` para aplicar todas as mudanças no banco de dados necessário para rodar a aplicação.
Após aplicar os migrations, execute `python3 manage.py loaddata initial_data.json` para carregar no banco de dados, informações pré cadastradas. Por padrão é criado um superusuário do Django com:
 - **Username**: admin
 - **Password**: magalu

Com todos os passos realizados, execute o servidor django com `python3 manage.py runserver 0:8000`, que iniciará na máquina do usuário um servidor de rede interna na porta 8000 para ser consumido.

Para verificar as informações cadastradas no banco de dados, acesse `http://localhost:8000/admin` e forneça as credenciais acima. Clicando em 'localizações' é possível ver, editar e remover entradas do banco de dados sem precisar utilizar o PGAdmin ou Psql. (com isso também é possível migrar bases de dados facilmente)