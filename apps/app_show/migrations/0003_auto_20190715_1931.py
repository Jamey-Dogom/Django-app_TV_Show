# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-15 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_show', '0002_auto_20190715_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(verbose_name='%m/%d/%Y'),
        ),
    ]
