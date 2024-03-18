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

from brex_webhooks_python_sdk.pydantic.update_webhook_subscription_status import UpdateWebhookSubscriptionStatus
from brex_webhooks_python_sdk.pydantic.webhook_event_type import WebhookEventType

class UpdateWebhookSubscriptionRequest(BaseModel):
    url: str = Field(alias='url')

    event_types: typing.List[WebhookEventType] = Field(alias='event_types')

    status: UpdateWebhookSubscriptionStatus = Field(alias='status')
    class Config:
        arbitrary_types_allowed = True
