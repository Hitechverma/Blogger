# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0026_auto_20160409_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='hashs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashname', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 16, 26, 47, 541036, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='hashtags',
            field=models.ManyToManyField(to='myblog.hashs'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 18, 16, 26, 47, 540124, tzinfo=utc)),
        ),
    ]
