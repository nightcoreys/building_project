# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0023_auto_20170507_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='img',
        ),
    ]
