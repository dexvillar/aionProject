# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0021_auto_20180311_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy_watche',
            name='user_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
