# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_auto_20160311_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 20, 57, 44, 653252, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='main',
            field=models.CharField(default=b'NO_name', max_length=100),
        ),
    ]
