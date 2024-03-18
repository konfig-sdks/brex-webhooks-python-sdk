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

from brex_webhooks_python_sdk.pydantic.user_attributes import UserAttributes
from brex_webhooks_python_sdk.pydantic.webhook_event_type import WebhookEventType

class UserUpdatedEvent(BaseModel):
    event_type: WebhookEventType = Field(alias='event_type')

    user_id: str = Field(alias='user_id')

    company_id: str = Field(alias='company_id')

    updated_attributes: typing.List[UserAttributes] = Field(alias='updated_attributes')
    class Config:
        arbitrary_types_allowed = True
