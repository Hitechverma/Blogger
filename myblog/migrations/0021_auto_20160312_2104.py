# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0020_auto_20160312_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 12, 21, 4, 23, 324716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='post',
            field=models.CharField(max_length=2000),
        ),
    ]
