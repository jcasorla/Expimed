# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-01-20 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0005_auto_20200118_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='med',
            name='category2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meds', to='dashboard_app.Category'),
        ),
    ]
