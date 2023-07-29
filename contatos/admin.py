from django.contrib import admin
from .models import Categoria, Contato

# Adicionando mais informações sobre o contato na area administrativa:
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'apelido', 'categoria', 'publicado',)  # 'telefone', 'email', 'data_criacao', )
    # Deixando o nome clicável para editar o contato:
    list_display_links = ('nome',)
    # Adicionando um filtro nos contatos:
    list_filter = ('categoria',)
    # Adicionando uma paginação, exibindo 10 contatos por pagina:
    list_per_page = 10
    # Campo de Busca:
    search_fields = ('nome', 'apelido', 'sobrenome', 'telefone')
    # Conseguir editar um campo sem precisar entrar no contato:
    list_editable = ('publicado', 'categoria', )


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
