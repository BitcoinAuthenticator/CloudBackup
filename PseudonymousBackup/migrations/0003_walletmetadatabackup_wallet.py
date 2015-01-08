# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
        ('PseudonymousBackup', '0002_auto_20150108_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='walletmetadatabackup',
            name='wallet',
            field=models.ForeignKey(default=0, to='Core.Wallet', unique=True),
            preserve_default=False,
        ),
    ]
