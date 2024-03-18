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

from brex_webhooks_python_sdk.type.expense_payment_status import ExpensePaymentStatus
from brex_webhooks_python_sdk.type.expense_payment_type import ExpensePaymentType
from brex_webhooks_python_sdk.type.money import Money
from brex_webhooks_python_sdk.type.webhook_event_type import WebhookEventType

class RequiredExpensePaymentStatusUpdatedEvent(TypedDict):
    event_type: WebhookEventType

    expense_id: str

    payment_status: ExpensePaymentStatus

    payment_type: ExpensePaymentType

class OptionalExpensePaymentStatusUpdatedEvent(TypedDict, total=False):
    #  This is the `id` returned in the [Get Company](https://developer.brex.com/openapi/webhooks_api/) endpoint. You can use the `company_id` to determine which access token to use when you get the details from our API endpoints. 
    company_id: str

    amount: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # The name of the card acceptor.
    payment_description: str

    # The ID of the card that is associated with the expense.
    card_id: str

class ExpensePaymentStatusUpdatedEvent(RequiredExpensePaymentStatusUpdatedEvent, OptionalExpensePaymentStatusUpdatedEvent):
    pass
