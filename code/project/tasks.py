from celery import shared_task
from django.utils import timezone
from .models import *
from datetime import date


@shared_task
def send_message():

    data_hoje = timezone.now().date()

    tasks_de_hoje = Task.objects.filter(data_fim=data_hoje)

    if tasks_de_hoje:
        for task in tasks_de_hoje:
            Mensagem.objects.create(
                titulo = f'Tarefa: {task.nome}',
                mensagem = f'A tarefa {task.nome} de {task.urgencia} que se iniciou no dia {task.data_inicio} encerra hoje, ao fim do dia',
                task_referente = task,
                user = task.agenda.user
            )

    return f'Quantidade de tasks proximas de finalizar = {tasks_de_hoje.count()}'