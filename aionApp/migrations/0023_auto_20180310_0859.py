# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0022_auto_20180310_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='user_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='watch_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sale',
            name='watch_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]