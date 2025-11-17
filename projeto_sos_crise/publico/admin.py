from django.contrib import admin
from .models import Doador, DoacaoFinanceira, DoacaoItem

class DoacaoItemInline(admin.TabularInline):
    # Isso permite ver os itens doados dentro da tela do Doador
    model = DoacaoItem
    extra = 0

@admin.register(Doador)
class DoadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')
    inlines = [DoacaoItemInline]

@admin.register(DoacaoFinanceira)
class DoacaoFinanceiraAdmin(admin.ModelAdmin):
    list_display = ('doador', 'valor', 'destino', 'pago', 'data')
    list_filter = ('pago', 'destino')