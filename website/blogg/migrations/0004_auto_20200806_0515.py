# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-06 05:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0003_auto_20200806_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 5, 15, 45, 839812, tzinfo=utc)),
        ),
    ]