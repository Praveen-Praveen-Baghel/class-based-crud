import os
from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "class_based_crud.settings")
app = Celery("class_based_crud")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


task_routes = {
    'class_based_crud.tasks.send_mail': {'queue': 'send-mail-queue'},
    'Class_based_crud.tasks.send_video': {'queue': 'send-video-queue'},
}

task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('send-mail-queue', Exchange('send-mail-queue'),
          routing_key='send-mail'),
    Queue('send-video-queue', Exchange('low-priority-queue'),
          routing_key='send-video'),
)
