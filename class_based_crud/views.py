from time import sleep
from django.db.models import Q
from .models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from .tasks import send_mail, send_video
from confluent_kafka import Consumer, KafkaError, Producer
from django.conf import settings


class Add(APIView):
    def post(self, request):
        data = request.data
        print(data)
        Employee.objects.create(
            ename=data.get("name"),
            cname=data.get("cname"),
            age=data.get("age"),
            passout=data.get("pass"),
            addr=data.get("addr"),
            econtact=data.get("contact"),
        )
        return Response(data)


class ListAll(APIView):
    def get(self, request):
        employees = Employee.objects.all().values()
        print(employees)
        return Response(employees)


class ListSearch(APIView):
    def get(self, request, id):
        employee = Employee.objects.get(eid=id)
        return Response(model_to_dict(employee))


class Update(APIView):
    def post(self, request, id):
        employee = Employee.objects.get(eid=id)
        employee.ename = request.data.get("name")
        employee.save()
        return Response({"status": "OK"})


class Delete(APIView):
    def post(self, request, id):
        Employee.objects.get(eid=id).delete()
        return Response({"status": "OK"})


class SendMail(APIView):
    def get(self, request):
        send_mail.apply_async(queue='send-mail-queue', routing_key='send-mail')
        # sleep(20)
        return Response({'status': 'ok'})


class SendVideo(APIView):
    def get(self, request):
        send_video.apply_async(queue='send-video-queue',
                               routing_key='send-video')
        # sleep(20)
        return Response({'status': 'ok'})


class SendMesage(APIView):
    def get(self, request):
        message = "Hello World!"
        topic = "salazar_message"
        producer = Producer(settings.KAFKA_CONFIG)
        producer.produce(topic, key=None, value=message)
        producer.flush()
        return Response({"status": "Message Sent"})


class ReceiveMessage(APIView):
    def get(self, request):
        topic = 'salazar_message'
        consumer = Consumer(settings.KAFKA_CONSUMER_CONFIG)
        consumer.subscribe([topic])

        while True:
            msg = consumer.poll(1.0)  # Adjust the polling timeout as needed

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print("Error while consuming: {}".format(msg.error()))
                    break

            print('Received message: ', str(msg.value()))
            
        consumer.close()
