from time import sleep
from celery import shared_task
from rest_framework.response import Response


@shared_task()
def send_mail():
    sleep(20)
