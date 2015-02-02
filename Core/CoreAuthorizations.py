__author__ = 'alonmuroch'

from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class BasicAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        if bundle.request.user is None:
            return False

        return object_list

    def read_detail(self, object_list, bundle):
        if bundle.obj is None:
            raise Unauthorized("You are not allowed to access that resource.")

    def create_list(self, object_list, bundle):
        if not bundle.request.user.is_authenticated():
            raise Unauthorized("You are not allowed to access that resource.")

        return object_list

    def create_detail(self, object_list, bundle):
        if not bundle.request.user.is_authenticated():
            raise Unauthorized("You are not allowed to access that resource.")
        return True

class UsersAuthorization(BasicAuthorization):
    def read_list(self, object_list, bundle):
        basicCheck = super(UsersAuthorization, self).read_list(object_list, bundle)
        if basicCheck is False:
            return False

        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(pk=bundle.request.user.pk)

    def read_detail(self, object_list, bundle):
        basic = super(UsersAuthorization, self).read_detail(object_list, bundle)
        if basic is False:
            return False

        if bundle.obj.pk is not bundle.request.user.pk:
            raise Unauthorized("You are not allowed to access that resource.")
        else:
            return True
    def create_detail(self, object_list, bundle):
        return True

class WalletAuthorization(BasicAuthorization):
    def read_list(self, object_list, bundle):
        basicCheck = super(WalletAuthorization, self).read_list(object_list, bundle)
        if basicCheck is False:
            return False

        # This assumes a ``QuerySet`` from ``ModelResource``.
        return object_list.filter(user=bundle.request.user)

    def read_detail(self, object_list, bundle):
        basic = super(WalletAuthorization, self).read_detail(object_list, bundle)
        if basic is False:
            return False

        if bundle.obj.user.pk is not bundle.request.user.pk:
            raise Unauthorized("You are not allowed to access that resource.")
        else:
            return True
