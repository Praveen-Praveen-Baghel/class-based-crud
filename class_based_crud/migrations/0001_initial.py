# Generated by Django 4.2.7 on 2023-11-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100, verbose_name='Name')),
                ('cname', models.CharField(max_length=100, verbose_name='College')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('passout', models.IntegerField(verbose_name='Passout')),
                ('addr', models.CharField(max_length=100, verbose_name='Address')),
                ('econtact', models.IntegerField(verbose_name='Phone')),
            ],
        ),
    ]
