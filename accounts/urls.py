from django.urls import path, include
from . import views

urlpatterns = [
    # Pagina inicial
    path('', views.login, name='index_login'),
    # Pagina onde faz o login:
    path('login/', views.login, name='login'),
    # Pagina de sair:
    path('logout/', views.logout, name='logout'),
    # Pagina onde se cadastra no site:
    path('register/', views.register, name='register'),
    # Pagina de dashboard quando está logado:
    path('dashboard/', views.dashboard, name='dashboard'),

]