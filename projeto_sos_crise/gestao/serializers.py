from rest_framework import serializers
from .models import ItemEstoque, PedidoAjuda

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEstoque
        fields = '__all__'

class PedidoAjudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoAjuda
        fields = '__all__'