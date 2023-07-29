from django.urls import path, include
from . import views

urlpatterns = [
    #Pagina inicial de tudo
    path('', views.index, name='index'),
    # Pagina inicial dos Clientes:
    path('index_contatos', views.index_contatos, name='index_contatos'),
    # Url do campo de pesquisa:
    path('busca/', views.busca, name='busca'),
    # Pagina de ver os detalhes do contato:
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),

]