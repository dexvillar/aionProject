# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0017_auto_20180310_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watche',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aionApp.user'),
        ),
    ]