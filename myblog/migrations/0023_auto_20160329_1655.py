# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0022_auto_20160313_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='post_title',
            field=models.CharField(default=b'blog', max_length=500),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 29, 16, 55, 24, 929431, tzinfo=utc)),
        ),
    ]
