# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-01-19 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0004_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='medcategory',
        ),
        migrations.AddField(
            model_name='med',
            name='category2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meds', to='dashboard_app.Category'),
        ),
    ]