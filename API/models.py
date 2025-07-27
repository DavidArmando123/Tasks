from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_vencimento = models.DateField()
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return f"{self.titulo} - {self.status}"
