# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hdconnect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x9c\xb0\xe5\x9d\x80')),
                ('cpu', models.CharField(max_length=32, verbose_name=b'cpu\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87')),
                ('mem', models.CharField(max_length=32, verbose_name=b'\xe5\x86\x85\xe5\xad\x98\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87')),
                ('disk', models.CharField(max_length=32, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98\xe4\xbd\xbf\xe7\x94\xa8\xe7\x8e\x87')),
                ('status', models.BooleanField(default=False, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x8a\xb6\xe6\x80\x81')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('delete_flag', models.CharField(max_length=4)),
            ],
        ),
    ]
