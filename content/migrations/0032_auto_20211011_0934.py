# Generated by Django 3.2.7 on 2021-10-11 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0031_auto_20211008_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Haber Linki'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 11, 9, 34, 33, 481263)),
        ),
    ]
