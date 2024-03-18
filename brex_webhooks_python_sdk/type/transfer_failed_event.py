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
from brex_webhooks_python_sdk.type.webhook_event_type import WebhookEventType

class RequiredTransferFailedEvent(TypedDict):
    event_type: WebhookEventType

    transfer_id: str

    payment_type: PaymentType

class OptionalTransferFailedEvent(TypedDict, total=False):
    # The original transaction ID that is returned when the payment type is ACH_RETURN, WIRE_RETURN and CHEQUE_RETURN.
    return_for_id: typing.Optional[str]

    #  This is the `id` returned in the [Get Company](https://developer.brex.com/openapi/webhooks_api/) endpoint. You can use the `company_id` to determine which access token to use when you get the details from our API endpoints. 
    company_id: str

class TransferFailedEvent(RequiredTransferFailedEvent, OptionalTransferFailedEvent):
    pass
