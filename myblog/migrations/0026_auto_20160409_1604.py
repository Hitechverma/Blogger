# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0025_auto_20160403_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 16, 4, 52, 358881, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 16, 4, 52, 358289, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='blogId',
            field=models.ForeignKey(to='myblog.userpost'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='hashtags',
            field=models.ManyToManyField(related_name='hashtags_rel_+', to='myblog.hashtag'),
        ),
    ]
