# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(),
        ),
    ]
