# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20170324_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_qtd',
            field=models.IntegerField(default=0),
        ),
    ]
