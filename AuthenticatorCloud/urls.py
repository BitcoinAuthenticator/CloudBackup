from django.conf.urls import patterns, include, url
from django.contrib import admin
from PseudonymousBackup.api import WalletMetaDataBackupResource
from Core.api import WalletsResource, UsersResource

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # PseudonymousBackup
    (r'^api/', include(WalletMetaDataBackupResource().urls)),

    # Core
    (r'^api/', include(WalletsResource().urls)),
    (r'^api/', include(UsersResource().urls)),
)
