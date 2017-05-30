# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-05-30 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0016_auto_20170529_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_path', models.ImageField(upload_to='Pimgage', verbose_name='图片路径')),
                ('img_name', models.CharField(max_length=50, verbose_name='图片名称')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_org', models.FileField(upload_to='pimage/1496136776.1504376/', verbose_name='Photo')),
                ('photo_small', models.CharField(max_length=255, verbose_name='Small')),
            ],
        ),
        migrations.AlterField(
            model_name='p_image',
            name='image_org',
            field=models.ImageField(upload_to='product_image/1496136776.1504376/', verbose_name='原图'),
        ),
    ]
