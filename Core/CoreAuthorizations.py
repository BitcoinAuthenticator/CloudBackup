__author__ = 'alonmuroch'

from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class UserAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        basicCheck = super(UserAuthorization, self).read_list(object_list, bundle)
        if basicCheck is False:
            return False

        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(pk=bundle.request.user.pk)

    def read_detail(self, object_list, bundle):
        basicCheck = super(UserAuthorization, self).read_detail(object_list, bundle)
        if basicCheck is False:
            raise Unauthorized("You are not allowed to access that resource.")

        # Is the requested object owned by the user?
        if bundle.obj.user is not bundle.request.user:
            raise Unauthorized("You are not allowed to access that resource.")
        else:
            return True



class WalletAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        basicCheck = super(WalletAuthorization, self).read_list(object_list, bundle)
        if basicCheck is False:
            return False

        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        basicCheck = super(WalletAuthorization, self).read_detail(object_list, bundle)
        if basicCheck is False:
            raise Unauthorized("You are not allowed to access that resource.")

        # Is the requested object owned by the user?
        if bundle.obj.user is not bundle.request.user:
            raise Unauthorized("You are not allowed to access that resource.")
        else:
            return True