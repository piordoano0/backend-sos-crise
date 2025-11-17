from rest_framework import viewsets
from .models import Doador, DoacaoFinanceira
from .serializers import DoadorSerializer, DoacaoFinanceiraSerializer

class DoadorViewSet(viewsets.ModelViewSet):
    """
    Permite cadastrar e ver doadores via API.
    """
    queryset = Doador.objects.all()
    serializer_class = DoadorSerializer

class DoacaoFinanceiraViewSet(viewsets.ModelViewSet):
    """
    Permite registrar doações financeiras via API.
    """
    queryset = DoacaoFinanceira.objects.all()
    serializer_class = DoacaoFinanceiraSerializer