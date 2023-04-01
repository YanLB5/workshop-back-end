# workshop-back-end
Workshop Fábrica de Software Backend - Yan  Lima Barbosa - P1


Nesse crud você terá uma biblioteca virtual que poderá cadastrar os livros da biblioteca, incluindo os seus respectivos títulos, autores e sua data de lançamento.

Você poderá cadastrar também os compradores dos livros, ou clientes, e seus respectivos dados, tais como: CPF, Telefone, Endereço.

Poderá também cadastrar o fornecedor de sua loja, com o CNPJ, e-mail e endereço do mesmo

=========================================================================================

É importante entender o que é REST é um estilo arquitetural que define um conjunto de restrições para criar serviços web escaláveis e de fácil manutenção. Um serviço web RESTful é aquele que segue essas restrições, como usar URIs para identificar recursos e usar métodos HTTP para realizar operações nesses recursos.

O termo "CRUD" é uma sigla em inglês que representa as quatro operações básicas usadas em bancos de dados relacionais: Create (criar), Read (ler), Update (atualizar) e Delete (excluir).

Essas operações são comumente usadas em sistemas de gerenciamento de bancos de dados (DBMS) para gerenciar o armazenamento, recuperação e atualização de dados.

CREATE (criar): a operação CREATE é usada para criar um novo registro em um banco de dados. Isso é feito inserindo uma nova linha na tabela correspondente ao registro, com os dados a serem armazenados.

READ (ler): a operação READ é usada para ler os dados armazenados em um banco de dados. Isso é feito por meio da seleção de uma ou mais linhas da tabela correspondente aos dados desejados.

UPDATE (atualizar): a operação UPDATE é usada para atualizar os dados armazenados em um banco de dados. Isso é feito alterando uma ou mais colunas em uma linha existente na tabela correspondente aos dados.

DELETE (excluir): a operação DELETE é usada para excluir um registro ou uma linha inteira em uma tabela de banco de dados.

Juntas, essas operações formam a base para a manipulação de dados em bancos de dados relacionais, permitindo que os usuários criem, leiam, atualizem e excluam registros, a fim de gerenciar e organizar grandes quantidades de informações de maneira eficiente.

==========================================================================================

CASO QUEIRA IMPLEMENTAR MAIS OPERAÇÕES CRUD EM DJANGO REST SIGA OS SEGUINTES PASSOS: 

Você irá irá precisar definir as suas views. As views no DRF (Django Rest Framework) são semelhantes às views regulares do Django, mas têm algumas diferenças. As views do DRF são chamadas de viewsets e são divididas em quatro tipos:

CreateAPIView: usada para criar um novo registro em seu banco de dados.
ListAPIView: usada para listar os registros existentes em seu banco de dados.
RetrieveAPIView: usada para recuperar um registro específico de seu banco de dados.
UpdateAPIView: usada para atualizar um registro específico em seu banco de dados.
DestroyAPIView: usada para excluir um registro específico de seu banco de dados.
Com isso em mente, você pode criar seu viewset. Você pode definir seu model e seu serializer. O serializer é usado para transformar o modelo em JSON, que é a forma em que a API irá enviar e receber dados.

Para cada operação CRUD, você precisa definir uma rota diferente. Isso pode ser feito usando o roteador do DRF. O roteador do DRF é uma maneira fácil de definir suas rotas de API. Você pode definir as rotas no arquivo urls.py do seu projeto Django.

Por exemplo, para definir uma rota para criar um novo registro em seu banco de dados, você pode usar o seguinte código:

from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet, basename='mymodel')
urlpatterns = router.urls
Isso criará uma rota em /mymodel/ que permitirá que os usuários enviem dados para criar um novo registro em seu banco de dados.

Para implementar as outras operações CRUD, basta criar as rotas correspondentes no arquivo urls.py e definir os métodos correspondentes em seu viewset.

Por fim, é importante lembrar que o DRF oferece recursos adicionais para a criação de API's RESTful, como autenticação, paginação e filtros. Você pode usar esses recursos para tornar sua API mais segura, escalável e fácil de usar.

Espero que isso tenha ajudado a entender como implementar as operações CRUD em Django usando REST!
