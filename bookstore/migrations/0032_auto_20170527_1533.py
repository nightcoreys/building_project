# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 15:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0031_auto_20170525_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='bookshelf',
            name='owner',
        ),
        migrations.AlterField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 27, 15, 33, 39, 305302, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='BookShelf',
        ),
    ]
