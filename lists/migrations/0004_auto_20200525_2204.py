# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-25 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
