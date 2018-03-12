# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0022_buy_watche_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy_watche',
            name='name',
        ),
        migrations.RemoveField(
            model_name='buy_watche',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='buy_watche',
            name='price',
        ),
        migrations.RemoveField(
            model_name='buy_watche',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='buy_watche',
            name='watch_id',
        ),
        migrations.AddField(
            model_name='buy_watche',
            name='watch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aionApp.watche'),
        ),
    ]
