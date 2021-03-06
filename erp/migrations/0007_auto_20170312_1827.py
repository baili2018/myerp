# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-03-12 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_auto_20170312_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upc',
            name='Asin',
            field=models.CharField(default='Null', max_length=12, null=True, verbose_name='对应ASIN'),
        ),
        migrations.AlterField(
            model_name='upc',
            name='Used',
            field=models.CharField(choices=[('Y', '是'), ('N', '否')], default='N', max_length=1, verbose_name='是否使用'),
        ),
        migrations.AlterField(
            model_name='upc',
            name='sku',
            field=models.CharField(default='Null', max_length=200, null=True, unique=True, verbose_name='对应SKU'),
        ),
    ]
