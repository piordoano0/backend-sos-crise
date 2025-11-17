from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import ItemEstoque, PedidoAjuda
from .serializers import EstoqueSerializer, PedidoAjudaSerializer

# --- PARTE 1: API PADRÃO (CRUD) ---
# Isso permite que o sistema crie, leia, atualize e delete itens via código

class EstoqueViewSet(viewsets.ModelViewSet):
    """
    API para controlar o Inventário (B2)
    """
    queryset = ItemEstoque.objects.all()
    serializer_class = EstoqueSerializer

class PedidoAjudaViewSet(viewsets.ModelViewSet):
    """
    API para criar e gerenciar Pedidos de Ajuda (B3)
    """
    queryset = PedidoAjuda.objects.all()
    serializer_class = PedidoAjudaSerializer


# --- PARTE 2: DASHBOARD PERSONALIZADO ---
# Essa função calcula os números para o gráfico da tela inicial (B1/A1)

def dashboard_admin(request):
    """
    Retorna JSON com estatísticas em tempo real para o Painel de Gestão.
    """
    # 1. Contar itens totais no estoque
    total_itens = 0
    estoque = ItemEstoque.objects.all()
    for item in estoque:
        total_itens += item.quantidade

    # 2. Contar pedidos urgentes que ainda estão abertos
    pedidos_urgentes = PedidoAjuda.objects.filter(prioridade_critica=True, status='ABERTO').count()

    # 3. Gerar lista de alertas (Itens acabando)
    alertas = []
    for item in estoque:
        # Verifica se a quantidade atual é menor que o mínimo definido na categoria
        if item.quantidade < item.categoria.nivel_critico:
            alertas.append(f"ALERTA: {item.nome} está acabando! (Restam {item.quantidade})")

    # Monta o pacote de dados
    dados = {
        "total_estoque": total_itens,
        "pedidos_criticos_pendentes": pedidos_urgentes,
        "lista_alertas": alertas,
        "status_sistema": "operacional"
    }
    
    return JsonResponse(dados)