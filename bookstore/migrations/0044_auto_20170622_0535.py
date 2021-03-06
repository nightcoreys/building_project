# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 05:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0043_auto_20170617_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.TextField(default='B1'),
        ),
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 22, 5, 35, 30, 120513, tzinfo=utc)),
        ),
    ]
