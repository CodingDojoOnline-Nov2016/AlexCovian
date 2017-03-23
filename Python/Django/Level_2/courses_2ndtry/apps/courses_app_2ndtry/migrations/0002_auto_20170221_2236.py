# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app_2ndtry', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='course',
            managers=[
                ('validation', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]