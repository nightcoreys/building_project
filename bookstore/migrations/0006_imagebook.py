# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20170422_1727'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(null=True, upload_to='img')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Book')),
            ],
        ),
    ]