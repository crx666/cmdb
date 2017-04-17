# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Hardware.BaseModel')),
                ('number', models.CharField(max_length=32, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe5\x8f\xb7')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('type', models.CharField(max_length=32, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('ip', models.CharField(max_length=32, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7ip')),
                ('service', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe6\x96\xb9\xe5\x90\x91')),
                ('statue', models.CharField(max_length=32, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe7\x8a\xb6\xe6\x80\x81')),
            ],
            bases=('Hardware.basemodel',),
        ),
        migrations.CreateModel(
            name='Asset_user',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Hardware.BaseModel')),
                ('asset_id', models.CharField(max_length=32, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7id')),
                ('user_id', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id')),
            ],
            bases=('Hardware.basemodel',),
        ),
    ]
