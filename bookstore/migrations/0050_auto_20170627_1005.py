# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 10:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0049_auto_20170627_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 27, 10, 5, 0, 813377, tzinfo=utc)),
        ),
    ]
