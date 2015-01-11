from django.contrib import admin
from PseudonymousBackup.models import WalletMetaDataBackup

class WalletMetaDataBackupAdmin(admin.ModelAdmin):
    list_display = ('id','wallet','last_updated')
    search_fields = ('id','wallet','last_updated')

admin.site.register(WalletMetaDataBackup,WalletMetaDataBackupAdmin)