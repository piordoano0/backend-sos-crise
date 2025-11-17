from django.contrib import admin
from .models import CategoriaItem, ItemEstoque, PedidoAjuda

@admin.register(ItemEstoque)
class EstoqueAdmin(admin.ModelAdmin):
    # Colunas que aparecem na tabela
    list_display = ('nome', 'categoria', 'quantidade', 'localizacao', 'status_estoque')
    # Filtros laterais
    list_filter = ('categoria', 'localizacao')
    # Barra de pesquisa
    search_fields = ('nome',)

    # Função para mostrar alerta visual se estiver acabando
    def status_estoque(self, obj):
        if obj.quantidade < obj.categoria.nivel_critico:
            return "⚠️ CRÍTICO"
        return "✅ Normal"
    status_estoque.short_description = "Status"

@admin.register(PedidoAjuda)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao_curta', 'status', 'prioridade_critica', 'data_criacao')
    list_filter = ('status', 'prioridade_critica')
    list_editable = ('status',) # Permite mudar o status direto na tabela sem abrir o item

    def descricao_curta(self, obj):
        return obj.descricao[:50] + "..."
    descricao_curta.short_description = "Necessidade"

# Registra a categoria simples
admin.site.register(CategoriaItem)