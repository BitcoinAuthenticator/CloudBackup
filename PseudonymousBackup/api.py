# PseudonymousBackup/api.py
from tastypie.resources import ModelResource
from PseudonymousBackup.models import WalletMetaDataBackup


class WalletMetaDataBackupResource(ModelResource):
    class Meta:
        queryset = WalletMetaDataBackup.objects.all()
        resource_name = 'WalletMetaDataBackup'