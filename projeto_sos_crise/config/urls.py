from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestao.views import dashboard_admin, EstoqueViewSet, PedidoAjudaViewSet
from publico.views import DoadorViewSet, DoacaoFinanceiraViewSet

# O Router cria as URLs da API automaticamente
router = DefaultRouter()

# Rotas da Gestão (Conjunto B)
router.register(r'estoque', EstoqueViewSet)
router.register(r'pedidos', PedidoAjudaViewSet)

# Rotas do Público (Conjunto A)
router.register(r'doadores', DoadorViewSet)
router.register(r'doacoes', DoacaoFinanceiraViewSet)

urlpatterns = [
    # Painel Administrativo (Visual)
    path('admin/', admin.site.urls),
    
    # Dashboard JSON (Personalizado)
    path('api/dashboard-stats/', dashboard_admin),
    
    # API Completa (Inclui todas as rotas registradas acima)
    path('api/', include(router.urls)),
]