# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-12 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_upc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upc',
            name='UPC',
            field=models.IntegerField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='UPC'),
        ),
    ]