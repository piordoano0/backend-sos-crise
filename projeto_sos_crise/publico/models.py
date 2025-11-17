from django.db import models

class Doador(models.Model):
    nome = models.CharField(max_length=200, blank=True, help_text="Pode ser anônimo")
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome if self.nome else "Doador Anônimo"

class DoacaoFinanceira(models.Model):
    OPCOES_VALOR = [
        (25.00, 'R$ 25,00'),
        (50.00, 'R$ 50,00'),
        (100.00, 'R$ 100,00'),
        (0.00, 'Outro Valor'),
    ]
    doador = models.ForeignKey(Doador, on_delete=models.SET_NULL, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    destino = models.CharField(max_length=100, default='Fundo Geral', help_text="Ex: Abrigo X ou Geral")
    metodo_pagamento = models.CharField(max_length=50, default='PIX')
    pago = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

class DoacaoItem(models.Model):
    CATEGORIAS = [
        ('ALIMENTO', 'Alimentos'),
        ('HIGIENE', 'Higiene'),
        ('ROUPA', 'Vestuário'),
        ('OUTRO', 'Outros'),
    ]
    doador = models.ForeignKey(Doador, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    descricao = models.CharField(max_length=255, help_text="Ex: 2 Pacotes de Fraldas G")
    quantidade = models.IntegerField()
    estado = models.CharField(max_length=20, choices=[('NOVO', 'Novo'), ('USADO', 'Usado')])
    precisa_coleta = models.BooleanField(default=False)
    endereco_coleta = models.TextField(blank=True, null=True)