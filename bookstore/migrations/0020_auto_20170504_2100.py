# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0019_auto_20170504_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(default='images.png', max_length=100),
        ),
    ]