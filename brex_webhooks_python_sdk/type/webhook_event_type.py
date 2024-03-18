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


WebhookEventType = Literal["REFERRAL_CREATED", "REFERRAL_ACTIVATED", "REFERRAL_APPLICATION_STATUS_CHANGED", "TRANSFER_PROCESSED", "TRANSFER_FAILED", "EXPENSE_PAYMENT_UPDATED", "USER_UPDATED"]
