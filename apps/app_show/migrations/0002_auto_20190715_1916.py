# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-15 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_show', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateTimeField(verbose_name='%m/%d/%Y'),
        ),
    ]
