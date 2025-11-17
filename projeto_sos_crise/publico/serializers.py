from rest_framework import serializers
from .models import Doador, DoacaoFinanceira, DoacaoItem

class DoacaoFinanceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoacaoFinanceira
        fields = '__all__'

class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        fields = '__all__'