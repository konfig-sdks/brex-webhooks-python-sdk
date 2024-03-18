# coding: utf-8

"""
    Webhooks API

     Brex uses webhooks to send real-time notifications when events happen in the accounts that you manage. Use webhook subscriptions to subscribe to different webhook events. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from brex_webhooks_python_sdk import schemas  # noqa: F401


class ExpensePaymentStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    `PENDING`:The transaction is yet to be captured. It may be approved, yet to be approved, or yet to be declined.

`DECLINED`: The transaction was declined.

    """
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("PENDING")
    
    @schemas.classproperty
    def DECLINED(cls):
        return cls("DECLINED")
