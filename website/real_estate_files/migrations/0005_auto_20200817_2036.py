# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-17 20:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_files', '0004_auto_20200817_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 20, 36, 36, 879974, tzinfo=utc)),
        ),
    ]
