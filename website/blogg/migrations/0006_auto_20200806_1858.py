# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-06 18:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0005_auto_20200806_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 18, 58, 16, 226959, tzinfo=utc)),
        ),
    ]
