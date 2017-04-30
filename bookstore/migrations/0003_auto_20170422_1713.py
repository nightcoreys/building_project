# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20170413_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Comics', 'Comics'), ('Novel', 'Novel')], default='Comics', max_length=256),
        ),
    ]
