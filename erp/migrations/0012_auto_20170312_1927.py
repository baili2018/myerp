# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-12 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0011_auto_20170312_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upc',
            name='sku',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='对应SKU'),
        ),
    ]
