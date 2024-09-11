from django.core.management.base import BaseCommand
from django.utils import timezone
from project.models import Task, Agenda
from django.db import connection

class Command(BaseCommand):
    help = 'Cria tasks com datas pertos de encerrar'

    def handle(self, *args, **kwargs):
        agenda_usada = Agenda.objects.get(pk=1)
        tasks_para_criar = []
        for indice in range(200):
            task = Task(
                nome = f'TASK{indice + 1}',
                descricao = f'Essa é a tarefa pendente {indice + 1}',
                data_inicio = timezone.now().date(),
                data_fim = timezone.now().date(),
                urgencia = 'URGENTE!!',
                agenda = agenda_usada,
            )
            tasks_para_criar.append(task)
        
        Task.objects.bulk_create(tasks_para_criar)
        
        self.stdout.write(self.style.SUCCESS('Todas as tasks foram criadas'))
