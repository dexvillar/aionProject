# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0044_auto_20180419_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_id', models.PositiveIntegerField(default=0)),
                ('total_sales', models.FloatField(default=0)),
                ('product_type', models.FloatField(default=0)),
                ('product', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='billing_addres',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='shipping_addres',
            name='user_id',
        ),
    ]
