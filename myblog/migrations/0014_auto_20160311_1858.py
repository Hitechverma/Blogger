# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0013_auto_20160310_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 11, 18, 58, 3, 355460, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='main',
            field=models.CharField(default=b'N0_name', max_length=100),
        ),
    ]
