# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-06 04:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0002_auto_20200806_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 4, 54, 32, 961408, tzinfo=utc)),
        ),
    ]
