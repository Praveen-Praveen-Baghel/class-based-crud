from django.db.models import Q
from .models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView


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
        return Response(
            {
                "id": employee.eid,
                "name": employee.ename,
                "college_name": employee.cname,
                "age": employee.age,
                "passout": employee.passout,
                "address": employee.addr,
                "contact": employee.econtact,
            }
        )


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
