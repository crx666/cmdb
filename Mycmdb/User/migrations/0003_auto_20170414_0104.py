# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auth_auth_role_myuser_role_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='delete_flag',
            field=models.CharField(default=b'Y', max_length=4, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe5\xbf\x97'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='make_time',
            field=models.DateTimeField(default=b'2017-03-15 20:30:20', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='role',
            name='enable',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u542f\u7528'),
        ),
    ]
