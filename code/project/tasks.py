from celery import shared_task
from django.utils import timezone
from .models import *
from datetime import date
from django.db import connection


@shared_task
def send_message():

    data_hoje = timezone.now().date()

    tasks_de_hoje = Task.objects.filter(data_fim=data_hoje)

    if tasks_de_hoje:
        for task in tasks_de_hoje:
            try:
                Mensagem.objects.get(task_referente=task)
                pass
            except Mensagem.DoesNotExist:
                Mensagem.objects.create(
                    titulo = f'Tarefa: {task.nome}',
                    mensagem = f'A tarefa {task.nome} de {task.urgencia} que se iniciou no dia {task.data_inicio} encerra hoje, ao fim do dia',
                    task_referente = task,
                    user = task.agenda.user
                )

    
    return f'Quantidade de tasks proximas de finalizar = {tasks_de_hoje.count()}'

def clear_message_box():
    data_hoje = timezone.now().date()


    mensagens_antigas = Mensagem.objects.all()

    for mensagem in mensagens_antigas:
        diferenca = data_hoje - mensagem.data_envio
        if diferenca.days >= 7:
            mensagem.delete()

    return 'Mensagens de 1 semana atrás foram deletadas'