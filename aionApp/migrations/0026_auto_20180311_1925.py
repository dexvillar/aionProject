# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0025_auto_20180311_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='month',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='checkout',
            name='year',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='card_number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='security_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
