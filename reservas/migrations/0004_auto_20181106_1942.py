# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20181025_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechareserva',
            name='reserva',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='reservas.Reserva'),
        ),
    ]
