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
from pydantic import BaseModel, Field, RootModel

from brex_webhooks_python_sdk.pydantic.webhook_subscription import WebhookSubscription

class PageWebhookSubscription(BaseModel):
    items: typing.List[WebhookSubscription] = Field(alias='items')

    next_cursor: typing.Optional[typing.Optional[str]] = Field(None, alias='next_cursor')
    class Config:
        arbitrary_types_allowed = True
