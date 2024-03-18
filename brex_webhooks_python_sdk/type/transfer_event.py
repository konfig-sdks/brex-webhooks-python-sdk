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

from brex_webhooks_python_sdk.type.payment_type import PaymentType
from brex_webhooks_python_sdk.type.transfer_failed_event import TransferFailedEvent
from brex_webhooks_python_sdk.type.transfer_processed_event import TransferProcessedEvent

class RequiredTransferEvent(TypedDict):
    company_id: str

    payment_type: PaymentType

class OptionalTransferEvent(TypedDict, total=False):
    return_for_id: typing.Optional[str]

class TransferEvent(RequiredTransferEvent, OptionalTransferEvent):
    pass
TransferEvent = typing.Union[TransferProcessedEvent,TransferFailedEvent]
