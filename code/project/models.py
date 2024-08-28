from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    rendimento = models.DecimalField(max_digits=3, decimal_places=1, default=10.0)

    def __str__(self):
        return self.username

class Agenda(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False, related_name='agenda')

    def __str__(self):
        return self.nome
    
    def agenda_de(self):
        return f'Agenda de {self.user.username}'
    

class Task(models.Model):
    urgencia_choices = (
        ('baixa', 'Não Urgente'),
        ('media', 'Media Prioridade'),
        ('alta', 'Alta Prioridade'),
        ('muito alta', 'URGENTE!!')
    )

    nome = models.CharField(max_length=60, null=False, blank=False)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    data_inicio = models.DateField(auto_now=False, auto_now_add=False)
    data_fim = models.DateField(auto_now=False, auto_now_add=False)
    urgencia = models.CharField(max_length=30, choices=urgencia_choices, null=False, blank=False)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, null=False, blank=False, )

    def __str__(self):
        return f'{self.nome} - {self.urgencia}'
    
class Mensagem(models.Model):
    titulo = models.CharField(max_length=30, null=False, blank=False)
    mensagem = models.TextField(null=False, blank=False)
    data_envio = models.DateField(auto_now_add=True)
    task_referente = models.ForeignKey(Task, on_delete=models.DO_NOTHING, null=False, blank=False, related_name='mensagens_enviadas')
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False, related_name='mensagens')
    
    def __str__(self):
        return f'Mensagem referente a task {self.task_referente.nome}'
    
    def get_task(self):
        return self.task_referente.nome