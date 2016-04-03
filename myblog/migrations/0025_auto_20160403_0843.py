# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0024_auto_20160402_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 3, 8, 43, 31, 556524, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 3, 8, 43, 31, 555898, tzinfo=utc)),
        ),
    ]
