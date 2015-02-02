from django.db import IntegrityError
from tastypie.exceptions import BadRequest

__author__ = 'alonmuroch'

# PseudonymousBackup/api.py
from django.conf.urls import url
from tastypie.resources import ModelResource
from Core.CoreAuthentication import CookieBasicAuthentication, UsersCookieBasicAuthentication
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden
from Core.CoreAuthorizations import WalletAuthorization, UsersAuthorization
from Core.models import Wallet
from django.contrib.auth.models import User
from tastypie import fields

class UsersResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'Users'
        authentication = UsersCookieBasicAuthentication()
        authorization  = UsersAuthorization()

    def obj_create(self, bundle, request=None, **kwargs):
        try:
            bundle = super(UsersResource, self).obj_create(bundle)
            bundle.obj.set_password(bundle.data.get('password'))
            bundle.obj.save()
        except IntegrityError:
            raise BadRequest('Username already exists')

        return bundle

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login/$" %
                (self._meta.resource_name),
                self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout/$' %
                (self._meta.resource_name),
                self.wrap_view('logout'), name='api_logout'),
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        # print request.POST
        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return self.create_response(request, {
                    'success': True,
                    'details': ('logged %s in' % (user.username))
                })
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'user is no longer active',
                    }, HttpForbidden )
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'Could not login, make sure your credentials are right',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)


class WalletsResource(ModelResource):
    user = fields.ForeignKey(UsersResource, 'user')
    class Meta:
        queryset = Wallet.objects.all()
        resource_name = 'Wallets'
        authentication = CookieBasicAuthentication()
        authorization = WalletAuthorization()