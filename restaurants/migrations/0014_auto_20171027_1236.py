# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_restaurant_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
