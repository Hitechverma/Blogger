# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_auto_20160311_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 11, 18, 58, 16, 77891, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='main',
            field=models.CharField(default=b'No_name', max_length=100),
        ),
    ]
