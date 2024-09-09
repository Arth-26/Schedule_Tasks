import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

app = Celery('setup')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_message': {
        'task': 'project.tasks.send_message',
        'schedule': 600.0,
    },
}