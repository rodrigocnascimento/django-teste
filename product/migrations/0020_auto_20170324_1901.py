# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20170324_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateTimeField(),
        ),
    ]