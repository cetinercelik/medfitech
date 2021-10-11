# Generated by Django 3.2.7 on 2021-10-01 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_auto_20211001_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentinput',
            name='corporate_descriptions',
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 1, 14, 10, 46, 535385)),
        ),
        migrations.AlterField(
            model_name='contentinput',
            name='blog_main_title',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Blog Üst Ana açıklama'),
        ),
        migrations.AlterField(
            model_name='contentinput',
            name='corporate_main_title',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Kurumsal Ana Başlık Açıklama'),
        ),
        migrations.AlterField(
            model_name='contentinput',
            name='software_main_title',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Yazılımlarımız Üst Ana açıklama'),
        ),
        migrations.AlterField(
            model_name='contentinput',
            name='team_main_title',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Ekibimiz Üst Ana açıklama'),
        ),
    ]
