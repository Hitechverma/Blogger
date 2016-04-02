# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0023_auto_20160329_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_data', models.CharField(max_length=200)),
                ('comment_time', models.DateTimeField(default=datetime.datetime(2016, 4, 2, 17, 56, 56, 375604, tzinfo=utc))),
                ('author', models.ForeignKey(to='myblog.user')),
            ],
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 17, 56, 56, 374960, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='comment',
            name='blogid',
            field=models.ForeignKey(to='myblog.userpost'),
        ),
    ]
