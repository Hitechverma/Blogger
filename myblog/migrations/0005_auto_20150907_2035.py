# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20150907_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 7, 20, 35, 1, 316765)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='username',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
