# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_userpost_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('User_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('access_token', models.CharField(max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 7, 20, 16, 20, 238884)),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='username',
            field=models.ForeignKey(to='myblog.user'),
        ),
    ]
