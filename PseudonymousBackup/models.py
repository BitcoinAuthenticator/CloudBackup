from django.db import models
from Core.models import Wallet


class WalletMetaDataBackup(models.Model):
    wallet = models.ForeignKey(Wallet, unique=True)
    meta_data = models.TextField()
    last_updated = models.DateTimeField('Last Updated')
