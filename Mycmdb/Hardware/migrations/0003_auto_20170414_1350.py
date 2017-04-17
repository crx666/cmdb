# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hardware', '0002_asset_asset_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='statue',
            field=models.BooleanField(default=True, verbose_name=b'\xe8\xb5\x84\xe4\xba\xa7\xe7\x8a\xb6\xe6\x80\x81'),
        ),
    ]
