# coding: utf-8
"""
    Webhooks API

     Brex uses webhooks to send real-time notifications when events happen in the accounts that you manage. Use webhook subscriptions to subscribe to different webhook events. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import typing
import inspect
from datetime import date, datetime
from brex_webhooks_python_sdk.client_custom import ClientCustom
from brex_webhooks_python_sdk.configuration import Configuration
from brex_webhooks_python_sdk.api_client import ApiClient
from brex_webhooks_python_sdk.type_util import copy_signature
from brex_webhooks_python_sdk.apis.tags.webhook_subscriptions_api import WebhookSubscriptionsApi



class BrexWebhooks(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.webhook_subscriptions: WebhookSubscriptionsApi = WebhookSubscriptionsApi(api_client)
