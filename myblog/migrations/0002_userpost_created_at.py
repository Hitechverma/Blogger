# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 27, 20, 56, 28, 85040)),
        ),
    ]
