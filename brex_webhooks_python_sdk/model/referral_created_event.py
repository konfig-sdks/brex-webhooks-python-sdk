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


class ReferralCreatedEvent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The webhook will be sent when a referral is created.
    """


    class MetaOapg:
        required = {
            "event_type",
            "referral_id",
        }
        
        class properties:
        
            @staticmethod
            def event_type() -> typing.Type['WebhookEventType']:
                return WebhookEventType
            referral_id = schemas.StrSchema
            __annotations__ = {
                "event_type": event_type,
                "referral_id": referral_id,
            }
    
    event_type: 'WebhookEventType'
    referral_id: MetaOapg.properties.referral_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> 'WebhookEventType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referral_id"]) -> MetaOapg.properties.referral_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_type", "referral_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> 'WebhookEventType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referral_id"]) -> MetaOapg.properties.referral_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_type", "referral_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        event_type: 'WebhookEventType',
        referral_id: typing.Union[MetaOapg.properties.referral_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReferralCreatedEvent':
        return super().__new__(
            cls,
            *args,
            event_type=event_type,
            referral_id=referral_id,
            _configuration=_configuration,
            **kwargs,
        )

from brex_webhooks_python_sdk.model.webhook_event_type import WebhookEventType
