# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0018_auto_20170504_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='photo',
        ),
        migrations.AddField(
            model_name='book',
            name='img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
