__author__ = 'alonmuroch'

from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from Core.models import Wallet


class WalletMetaDataBackupAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        basicCheck = super(WalletMetaDataBackupAuthorization, self).read_list(object_list, bundle)
        if basicCheck is False:
            return False

        usersWallets = Wallet.objects.filter(user=bundle.request.user)

        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(wallet__in=usersWallets)

    def read_detail(self, object_list, bundle):
        basicCheck = super(WalletMetaDataBackupAuthorization, self).read_detail(object_list, bundle)
        if basicCheck is False:
            raise Unauthorized("You are not allowed to access that resource.")

        # Is the requested object owned by the user?
        if bundle.obj.user is not bundle.request.user:
            raise Unauthorized("You are not allowed to access that resource.")
        else:
            return True