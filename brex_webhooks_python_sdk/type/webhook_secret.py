# coding: utf-8

"""
    Webhooks API

     Brex uses webhooks to send real-time notifications when events happen in the accounts that you manage. Use webhook subscriptions to subscribe to different webhook events. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from brex_webhooks_python_sdk.type.webhook_secret_status import WebhookSecretStatus

class RequiredWebhookSecret(TypedDict):
    secret: str

    status: WebhookSecretStatus

class OptionalWebhookSecret(TypedDict, total=False):
    pass

class WebhookSecret(RequiredWebhookSecret, OptionalWebhookSecret):
    pass
