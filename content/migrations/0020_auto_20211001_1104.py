# Generated by Django 3.2.7 on 2021-10-01 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_auto_20211001_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentinput',
            name='branch_email',
        ),
        migrations.RemoveField(
            model_name='contentinput',
            name='central_email',
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 1, 11, 4, 14, 358984)),
        ),
    ]
