# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0022_auto_20170507_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(default='/static/bookstore/images.png', max_length=100),
        ),
    ]