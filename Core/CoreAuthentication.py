__author__ = 'alonmuroch'

from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication

class CookieBasicAuthentication(BasicAuthentication):
    '''
     If the user is already authenticated by a django session it will
     allow the request (useful for ajax calls) . If it is not, defaults
     to basic authentication, which other clients could use.
    '''
    def __init__(self, *args, **kwargs):
        super(CookieBasicAuthentication, self).__init__(*args, **kwargs)

    def is_authenticated(self, request, **kwargs):
        from django.contrib.sessions.models import Session
        if 'sessionid' in request.COOKIES:
            try:
               s = Session.objects.get(pk=request.COOKIES['sessionid'])
            except Session.DoesNotExist:
               s = None

            if s is not None and '_auth_user_id' in s.get_decoded():
                u = User.objects.get(id=s.get_decoded()['_auth_user_id'])
                request.user = u
                return True
        return super(CookieBasicAuthentication, self).is_authenticated(request, **kwargs)


class UsersCookieBasicAuthentication(CookieBasicAuthentication):
    def is_authenticated(self, request, **kwargs):
        '''
            Anyone can create a user.
        '''
        if request.method == "POST":
            return True
        else:
            return super(UsersCookieBasicAuthentication, self).is_authenticated(request, **kwargs)