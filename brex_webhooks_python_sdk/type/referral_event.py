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

from brex_webhooks_python_sdk.type.referral_activated_event import ReferralActivatedEvent
from brex_webhooks_python_sdk.type.referral_application_status_changed_event import ReferralApplicationStatusChangedEvent
from brex_webhooks_python_sdk.type.referral_created_event import ReferralCreatedEvent

ReferralEvent = typing.Union[ReferralCreatedEvent,ReferralActivatedEvent,ReferralApplicationStatusChangedEvent]
ReferralEvent = object
