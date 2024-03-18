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


class ExpensePaymentType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    `PURCHASE`: A pending transaction for making a purchase.

`REFUND`: A pending transaction for a refund.

`WITHDRAWAL`: A pending transaction for a withdrawal.

`DECLINED`: A pending transaction that was declined and will not be completed.

    """


    class MetaOapg:
        enum_value_to_name = {
            "PURCHASE": "PURCHASE",
            "REFUND": "REFUND",
            "WITHDRAWAL": "WITHDRAWAL",
            "DECLINED": "DECLINED",
        }
    
    @schemas.classproperty
    def PURCHASE(cls):
        return cls("PURCHASE")
    
    @schemas.classproperty
    def REFUND(cls):
        return cls("REFUND")
    
    @schemas.classproperty
    def WITHDRAWAL(cls):
        return cls("WITHDRAWAL")
    
    @schemas.classproperty
    def DECLINED(cls):
        return cls("DECLINED")
