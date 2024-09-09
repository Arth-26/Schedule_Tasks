from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class Command(BaseCommand):
    help = 'Cria o agendamento de verificação de tarefas'

    def handle(self, *args, **kwargs):
        intervalo, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.MINUTES
        )

        if created:
            PeriodicTask.objects.get_or_create(
                interval=intervalo,
                name='Verificar tarefas pendentes',
                task='project.tasks.send_message',
                args=json.dumps([])
            )
            self.stdout.write(self.style.SUCCESS('Schedule criada com sucesso'))
        else:
            self.stdout.write(self.style.SUCCESS('Schedule já existe'))