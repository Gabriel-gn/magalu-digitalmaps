*  Para construir e executar essa imagem sem o docker compose, executar (nesta pasta):

`docker build -t digitalmaps_postgres .`

*  Para executar a imagem em container corretamente, executar:

`docker run -d -p 5432:5432 -v pgdata:/var/lib/postgresql/data/ -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=magalu -e POSTGRES_DB=digitalmaps -e PGDATA=/data/postgres --name digitalmaps_postgres digitalmaps_postgres`

*  Com o container criado com o nome "digitalmaps_postgres", caso seja necessário pará-lo (`docker stop digitalmaps_postgres` / `docker kill digitalmaps_postgres`), é possível reiniciá-lo com o comando `docker start digitalmaps_postgres`

Alterar as variáveis de ambiente do comando de execução do container de acordo com a necessidade:
*  POSTGRES_USER=postgres - usuário padrão da base
*  POSTGRES_PASSWORD=magalu - senha do usuário padrão da base
*  POSTGRES_DB=digitalmaps - nome da database a ser criada
*  PGDATA=/data/postgres - onde dados serão armazenados em volume de docker