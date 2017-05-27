# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 15:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0032_auto_20170527_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default='Comics', on_delete=django.db.models.deletion.CASCADE, to='bookstore.Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 27, 15, 38, 14, 548763, tzinfo=utc)),
        ),
    ]