__author__ = 'alonmuroch'

import BaseTest

class CoreTest(BaseTest):


    def test_wallet_resource(self):
        result = self.api_client.get("/api/Wallets/", format='json')
        print result
