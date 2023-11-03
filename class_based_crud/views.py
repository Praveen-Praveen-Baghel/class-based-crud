from time import sleep
from django.db.models import Q
from .models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from .tasks import send_mail


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
        send_mail.delay()
        # sleep(20)
        return Response({'status': 'ok'})
