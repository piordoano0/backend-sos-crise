from django.db import models

class CategoriaItem(models.Model):
    nome = models.CharField(max_length=100) # Ex: Água, Colchonetes
    nivel_critico = models.IntegerField(default=10, help_text="Avisar se o estoque cair abaixo disso")
    
    def __str__(self):
        return self.nome

class ItemEstoque(models.Model):
    categoria = models.ForeignKey(CategoriaItem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200) 
    quantidade = models.IntegerField(default=0)
    validade = models.DateField(null=True, blank=True)
    localizacao = models.CharField(max_length=100, help_text="Local no armazém")

    def __str__(self):
        return f"{self.nome} - Qtd: {self.quantidade}"

class PedidoAjuda(models.Model):
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto - Não atendido'),
        ('TRIAGEM', 'Em Separação'),
        ('ROTA', 'Em Rota de Entrega'),
        ('CONCLUIDO', 'Entregue/Concluído'),
    ]
    descricao = models.TextField(help_text="Ex: Abrigo São José precisa de 50 cobertores")
    prioridade_critica = models.BooleanField(default=False, help_text="Marcar se for URGENTE")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTO')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # B4: Logística
    motorista_responsavel = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        alerta = "🚨 " if self.prioridade_critica else ""
        return f"{alerta}Pedido {self.id}: {self.status}"