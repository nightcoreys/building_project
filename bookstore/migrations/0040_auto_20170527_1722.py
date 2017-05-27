# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 17:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0039_auto_20170527_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='avg_rating',
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 27, 17, 22, 20, 280006, tzinfo=utc)),
        ),
    ]
