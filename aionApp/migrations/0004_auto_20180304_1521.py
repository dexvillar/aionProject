# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0003_auto_20180304_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
