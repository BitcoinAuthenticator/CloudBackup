from django.db import models
from Core.models import Wallet
from datetime import datetime


class WalletMetaDataBackup(models.Model):
    wallet = models.ForeignKey(Wallet, unique=True)
    meta_data = models.TextField()
    last_updated = models.DateTimeField('Last Updated', default=datetime.now())

    def __unicode__(self):
        return self.wallet.name
