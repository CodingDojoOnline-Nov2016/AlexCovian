# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 23:35
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('emailvalidate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='email',
            managers=[
                ('validation', django.db.models.manager.Manager()),
            ],
        ),
    ]
