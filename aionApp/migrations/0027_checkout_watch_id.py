# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0026_auto_20180311_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='watch_id',
            field=models.IntegerField(default=0),
        ),
    ]