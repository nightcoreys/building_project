# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0021_auto_20170504_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(max_length=100),
        ),
    ]