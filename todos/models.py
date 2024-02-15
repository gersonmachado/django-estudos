from django.db import models

# Create your models here.
# Cada atributo da classe corresponde a uma coluna do bd


class Todo(models.Model):
    # Definindo o tipo do campo e regras
    title = models.CharField(max_length=100, null=False, blank=False)  
    # Para adicionar automaticamente as inf de agora [auto_now_add TRUE]
    criated_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)  
    deadline = models.DateField(null=False, blank=False)
    # Aceita valor nulo pois é uma tarefa que não foi finalizada [null TRUE]
    finalizado = models.DateField(null=True)  

    # Classe Meta para ordenar a lista.
    # a coluna "deadline" foi selecionada para ordenar a exibição da lista de tarefas
    class Meta:
        ordering = ["deadline"]
