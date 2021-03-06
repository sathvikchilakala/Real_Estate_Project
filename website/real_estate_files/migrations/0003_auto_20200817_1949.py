# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-17 19:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_files', '0002_auto_20200806_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enqdb',
            old_name='agent',
            new_name='agent_name',
        ),
        migrations.RenameField(
            model_name='enqdb',
            old_name='mail',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='enqdb',
            old_name='name',
            new_name='contact_name',
        ),
        migrations.RenameField(
            model_name='enqdb',
            old_name='mno',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='enqdb',
            old_name='message',
            new_name='property_description',
        ),
        migrations.AlterField(
            model_name='post',
            name='Your_Name_REGISTRATION_REQUIRED',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 19, 49, 32, 735000, tzinfo=utc)),
        ),
    ]
