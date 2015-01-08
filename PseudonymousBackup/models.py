from django.db import models


class WalletMetaDataBackup(models.Model):
    meta_data = models.TextField()
    last_updated = models.DateTimeField('date published')