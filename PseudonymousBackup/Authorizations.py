from Core.models import Wallet

__author__ = 'alonmuroch'

from Core.CoreAuthorizations import BasicAuthorization
from tastypie.exceptions import Unauthorized


class BackupAuthorization(BasicAuthorization):
    def read_list(self, object_list, bundle):
        basicCheck = super(BackupAuthorization, self).read_list(object_list, bundle)
        if basicCheck is False:
            return False

        user_wallets = Wallet.objects.filter(user=bundle.request.user)

        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(wallet__in=user_wallets)

    def read_detail(self, object_list, bundle):
        basic = super(BackupAuthorization, self).read_detail(object_list, bundle)
        if basic is False:
            return False

        wallet = bundle.obj.wallet
        if wallet.user.pk is not bundle.request.user.pk:
            raise Unauthorized("You are not allowed to access that resource.")
        else:
            return True