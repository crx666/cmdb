# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('select_host', models.BooleanField(default=False, verbose_name='\u67e5\u770b\u8d44\u4ea7')),
                ('edit_host', models.BooleanField(default=False, verbose_name='\u4fee\u6539\u8d44\u4ea7')),
                ('add_host', models.BooleanField(default=False, verbose_name='\u6dfb\u52a0\u4e3b\u673a')),
                ('delete_host', models.BooleanField(default=False, verbose_name='\u5220\u9664\u8d44\u4ea7')),
                ('add_user', models.BooleanField(default=False, verbose_name='\u6dfb\u52a0\u7528\u6237')),
                ('edit_user', models.BooleanField(default=False, verbose_name='\u4fee\u6539\u7528\u6237')),
                ('edit_pass', models.BooleanField(default=False, verbose_name='\u4fee\u6539\u5bc6\u7801')),
                ('delete_user', models.BooleanField(default=False, verbose_name='\u5220\u9664\u7528\u6237')),
            ],
        ),
        migrations.CreateModel(
            name='Auth_Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_id', models.CharField(max_length=32, verbose_name=b'\xe6\x9d\x83\xe9\x99\x90id')),
                ('role_id', models.CharField(max_length=32, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2id')),
            ],
        ),
        migrations.CreateModel(
            name='Myuser_Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id')),
                ('role_id', models.CharField(max_length=32, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2id')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=32, verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe5\x90\x8d')),
                ('role_dis', models.TextField(verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
        ),
    ]
