__author__ = 'alonmuroch'

from tastypie.test import ResourceTestCase
from django.contrib.auth.models import User

class BaseTest(ResourceTestCase):

    fixtures = ['dump.json']

    def setUp(self):
        super(BaseTest, self).setUp()
        self.testuser1 = User.object.get(UserName="testuser1")
        self.testuser2 = User.object.get(UserName="testuser2")
        self.testuser3 = User.object.get(UserName="testuser3")
        self.testuser4 = User.object.get(UserName="testuser4")

    def get_credentials(self):
        pass