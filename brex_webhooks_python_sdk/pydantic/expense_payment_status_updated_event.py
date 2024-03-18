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

from brex_webhooks_python_sdk.pydantic.expense_payment_status import ExpensePaymentStatus
from brex_webhooks_python_sdk.pydantic.expense_payment_type import ExpensePaymentType
from brex_webhooks_python_sdk.pydantic.money import Money
from brex_webhooks_python_sdk.pydantic.webhook_event_type import WebhookEventType

class ExpensePaymentStatusUpdatedEvent(BaseModel):
    event_type: WebhookEventType = Field(alias='event_type')

    expense_id: str = Field(alias='expense_id')

    payment_status: ExpensePaymentStatus = Field(alias='payment_status')

    payment_type: ExpensePaymentType = Field(alias='payment_type')

    #  This is the `id` returned in the [Get Company](https://developer.brex.com/openapi/webhooks_api/) endpoint. You can use the `company_id` to determine which access token to use when you get the details from our API endpoints. 
    company_id: typing.Optional[str] = Field(None, alias='company_id')

    amount: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='amount')

    # The name of the card acceptor.
    payment_description: typing.Optional[str] = Field(None, alias='payment_description')

    # The ID of the card that is associated with the expense.
    card_id: typing.Optional[str] = Field(None, alias='card_id')
    class Config:
        arbitrary_types_allowed = True
