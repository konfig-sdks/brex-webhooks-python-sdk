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

from brex_webhooks_python_sdk.pydantic.payment_type import PaymentType
from brex_webhooks_python_sdk.pydantic.webhook_event_type import WebhookEventType

class TransferFailedEvent(BaseModel):
    event_type: WebhookEventType = Field(alias='event_type')

    transfer_id: str = Field(alias='transfer_id')

    payment_type: PaymentType = Field(alias='payment_type')

    # The original transaction ID that is returned when the payment type is ACH_RETURN, WIRE_RETURN and CHEQUE_RETURN.
    return_for_id: typing.Optional[typing.Optional[str]] = Field(None, alias='return_for_id')

    #  This is the `id` returned in the [Get Company](https://developer.brex.com/openapi/webhooks_api/) endpoint. You can use the `company_id` to determine which access token to use when you get the details from our API endpoints. 
    company_id: typing.Optional[str] = Field(None, alias='company_id')
    class Config:
        arbitrary_types_allowed = True
