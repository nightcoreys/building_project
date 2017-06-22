# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-17 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0042_auto_20170528_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.TextField(default='B1'),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 18, 9, 52, 118573, tzinfo=utc)),
        ),
    ]
