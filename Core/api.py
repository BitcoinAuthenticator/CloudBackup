__author__ = 'alonmuroch'

# PseudonymousBackup/api.py
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden
from Core.CoreAuthorizations import UserAuthorization, WalletAuthorization

from Core.models import Wallet
from django.contrib.auth.models import User

class WalletsResource(ModelResource):
    class Meta:
        queryset = Wallet.objects.all()
        resource_name = 'Wallets'
        authentication = SessionAuthentication()
        authorization = WalletAuthorization()

class UsersResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'Users'
        authentication = SessionAuthentication()
        authorization = UserAuthorization()

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
                    'reason': 'disabled',
                    }, HttpForbidden )
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)
