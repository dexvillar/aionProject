# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0030_auto_20180312_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviews',
            field=models.CharField(max_length=2048),
        ),
    ]
