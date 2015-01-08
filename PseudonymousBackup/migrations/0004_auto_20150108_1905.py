# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PseudonymousBackup', '0003_walletmetadatabackup_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletmetadatabackup',
            name='last_updated',
            field=models.DateTimeField(verbose_name=b'Last Updated'),
            preserve_default=True,
        ),
    ]
