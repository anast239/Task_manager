# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-24 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_manager', '0002_task_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]