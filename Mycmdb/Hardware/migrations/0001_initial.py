# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delete_flag', models.CharField(max_length=4, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe5\xbf\x97')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Hardware.BaseModel')),
                ('hostname', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d')),
                ('ip', models.CharField(max_length=32, verbose_name=b'ip')),
                ('Mac', models.CharField(max_length=32, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe5\x9c\xb0\xe5\x9d\x80')),
                ('cpu', models.CharField(max_length=32, verbose_name=b'cpu')),
                ('Mem', models.CharField(max_length=32, verbose_name=b'\xe5\x86\x85\xe5\xad\x98')),
                ('Disk', models.CharField(max_length=32, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98')),
                ('system', models.CharField(max_length=32, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('IO', models.CharField(max_length=32, verbose_name=b'IO')),
                ('lastLogin', models.DateTimeField(verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95\xe6\x97\xb6\xe9\x97\xb4')),
                ('lastLoginUser', models.IntegerField(verbose_name=b'\xe4\xb8\x8a\xe6\xac\xa1\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7')),
                ('isActive', models.CharField(max_length=32, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe8\xa2\xab\xe6\xbf\x80\xe6\xb4\xbb')),
            ],
            bases=('Hardware.basemodel',),
        ),
    ]
