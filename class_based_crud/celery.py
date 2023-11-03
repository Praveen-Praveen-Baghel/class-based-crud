import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "class_based_crud.settings")
app = Celery("class_based_crud")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

