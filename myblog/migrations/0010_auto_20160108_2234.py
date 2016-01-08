# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0009_auto_20150907_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='main',
            field=models.CharField(default=b'NO_name', max_length=100),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 8, 22, 34, 2, 238082)),
        ),
    ]
