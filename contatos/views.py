from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator
from .models import Contato
# Esse Q serve para realizar consultas mais complexas
from django.db.models import Q, Value
# Aqui vou usar o Concat para aprimorar a consulta:
from django.db.models.functions import Concat
# Importando as mensagens de alerta
from django.contrib import messages


def index(request):
    return render(request, 'contatos/index.html')

def index_contatos(request):
    # Serão exibidos em ordem alfabetica dos nomes e so os que estiverem marcado como publicado:
    contatos = Contato.objects.order_by('nome').filter(publicado=True)
    # Criando uma paginação, 10 contatos por pagina:
    paginator = Paginator(contatos, 10)
    #
    page = request.GET.get('page')
    #
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index_contatos.html', {
                 'contatos': contatos
                  })

# FUNÇÕES DA PAGINA DE VISUALIZAR UM CONTATO:
def ver_contato(request, contato_id):
    # Levantar error 404 quando não existe uma pagina, por exemplo | (get_object_or_404)
    contato = get_object_or_404(Contato, id=contato_id)
    # Se entrar no link de ID que nao ta publicado:
    if not contato.publicado:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
                 'contato': contato
                  })

# FUNÇÕES DO CAMPO DE BUSCA DA AGENDA:
def busca(request):
    # Obtendo o valor que está vindo do termo (campo de pesquisa):
    termo = request.GET.get('termo')

    # Se não ter nada no termo de pesquisa, levanta erro de 404(page not found)
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo não pode estar vazio.')
        return redirect('index_contato')

    # Unindo valores para otimizar a busca:
    campos = Concat('nome', Value(' '), 'sobrenome')
    # Filtrando a pesquisa:
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    # Oberservando como ta sendo feita a pesquisa em SQL:
    """print(contatos.query)"""
    #
    paginator = Paginator(contatos, 10)
    #
    page = request.GET.get('page')
    #
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
                 'contatos': contatos
                  })