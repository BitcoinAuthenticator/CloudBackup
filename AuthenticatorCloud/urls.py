from django.conf.urls import patterns, include, url
from django.contrib import admin
from PseudonymousBackup.api import WalletMetaDataBackupResource

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(WalletMetaDataBackupResource().urls)),
)
