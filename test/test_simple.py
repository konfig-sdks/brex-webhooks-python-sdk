# coding: utf-8

"""
    Webhooks API

     Brex uses webhooks to send real-time notifications when events happen in the accounts that you manage. Use webhook subscriptions to subscribe to different webhook events. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest

import os
from pprint import pprint
from brex_webhooks_python_sdk import BrexWebhooks

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        brexwebhooks = BrexWebhooks(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',,
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(brexwebhooks)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
