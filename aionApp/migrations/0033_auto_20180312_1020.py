# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aionApp', '0032_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='billing_add',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='aionApp.billing_addres'),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_add',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='aionApp.shipping_addres'),
        ),
    ]