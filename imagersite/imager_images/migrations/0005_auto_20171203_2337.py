# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0004_auto_20171128_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]