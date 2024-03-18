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
from brex_webhooks_python_sdk.pydantic.transfer_failed_event import TransferFailedEvent
from brex_webhooks_python_sdk.pydantic.transfer_processed_event import TransferProcessedEvent

class TransferEvent(BaseModel):
    company_id: str = Field(alias='company_id')

    payment_type: PaymentType = Field(alias='payment_type')

    return_for_id: typing.Optional[typing.Optional[str]] = Field(None, alias='return_for_id')
    class Config:
        arbitrary_types_allowed = True
TransferEvent = typing.Union[TransferProcessedEvent,TransferFailedEvent]
