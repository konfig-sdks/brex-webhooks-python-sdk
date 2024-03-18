# coding: utf-8

"""
    Webhooks API

     Brex uses webhooks to send real-time notifications when events happen in the accounts that you manage. Use webhook subscriptions to subscribe to different webhook events. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest
from unittest.mock import patch

import urllib3

import brex_webhooks_python_sdk
from brex_webhooks_python_sdk.paths.v1_webhooks_id import delete
from brex_webhooks_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1WebhooksId(ApiTestMixin, unittest.TestCase):
    """
    V1WebhooksId unit test stubs
        Unregister Webhook
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
