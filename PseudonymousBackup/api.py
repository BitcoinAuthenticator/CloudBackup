# PseudonymousBackup/api.py
from Core.CoreAuthentication import DjangoCookieBasicAuthentication
from Core.CoreAuthorizations import BasicAuthorization
from Core.api import WalletsResource
from tastypie.resources import ModelResource
from PseudonymousBackup.models import WalletMetaDataBackup
from tastypie import fields

class WalletMetaDataBackupResource(ModelResource):
    wallet = fields.ForeignKey(WalletsResource, 'wallet')
    class Meta:
        queryset = WalletMetaDataBackup.objects.all()
        resource_name = 'WalletMetaDataBackup'
        authentication = DjangoCookieBasicAuthentication()
        authorization = BasicAuthorization()