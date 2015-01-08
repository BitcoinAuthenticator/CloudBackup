# PseudonymousBackup/api.py
from tastypie.resources import ModelResource
from PseudonymousBackup.models import WalletMetaDataBackup
from tastypie.authentication import SessionAuthentication
from Authorizations import WalletMetaDataBackupAuthorization

class WalletMetaDataBackupResource(ModelResource):
    class Meta:
        queryset = WalletMetaDataBackup.objects.all()
        resource_name = 'WalletMetaDataBackup'
        authentication = SessionAuthentication()
        authorization = WalletMetaDataBackupAuthorization()