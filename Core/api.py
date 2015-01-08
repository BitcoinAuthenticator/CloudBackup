__author__ = 'alonmuroch'

# PseudonymousBackup/api.py
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
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