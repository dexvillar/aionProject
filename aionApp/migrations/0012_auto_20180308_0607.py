# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0011_auto_20180308_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='watch_id',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='watch_id',
        ),
        migrations.RemoveField(
            model_name='watche',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='watche',
            name='watch_id',
        ),
        migrations.AddField(
            model_name='billing_addres',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='checkout',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='shipping_addres',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='watche',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]