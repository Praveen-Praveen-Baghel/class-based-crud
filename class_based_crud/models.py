from django.db import models


class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100, verbose_name="Name")
    cname = models.CharField(max_length=100, verbose_name="College")
    age = models.IntegerField(verbose_name="Age")
    passout = models.IntegerField(verbose_name="Passout")
    addr = models.CharField(max_length=100, verbose_name="Address")
    econtact = models.IntegerField(verbose_name="Phone")
