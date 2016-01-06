# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_auto_20150907_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 7, 20, 49, 46, 162574)),
        ),
    ]
