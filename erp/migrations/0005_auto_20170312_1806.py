# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-12 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20170312_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upc',
            name='UPC',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='UPC'),
        ),
    ]