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


class TransferProcessedEvent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The webhook will be sent when a transfer is processed.
    """


    class MetaOapg:
        required = {
            "payment_type",
            "event_type",
            "transfer_id",
        }
        
        class properties:
        
            @staticmethod
            def event_type() -> typing.Type['WebhookEventType']:
                return WebhookEventType
            transfer_id = schemas.StrSchema
        
            @staticmethod
            def payment_type() -> typing.Type['PaymentType']:
                return PaymentType
            
            
            class return_for_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'return_for_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            company_id = schemas.StrSchema
            __annotations__ = {
                "event_type": event_type,
                "transfer_id": transfer_id,
                "payment_type": payment_type,
                "return_for_id": return_for_id,
                "company_id": company_id,
            }
    
    payment_type: 'PaymentType'
    event_type: 'WebhookEventType'
    transfer_id: MetaOapg.properties.transfer_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> 'WebhookEventType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_id"]) -> MetaOapg.properties.transfer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_type"]) -> 'PaymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["return_for_id"]) -> MetaOapg.properties.return_for_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_type", "transfer_id", "payment_type", "return_for_id", "company_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> 'WebhookEventType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_id"]) -> MetaOapg.properties.transfer_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_type"]) -> 'PaymentType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["return_for_id"]) -> typing.Union[MetaOapg.properties.return_for_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> typing.Union[MetaOapg.properties.company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_type", "transfer_id", "payment_type", "return_for_id", "company_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payment_type: 'PaymentType',
        event_type: 'WebhookEventType',
        transfer_id: typing.Union[MetaOapg.properties.transfer_id, str, ],
        return_for_id: typing.Union[MetaOapg.properties.return_for_id, None, str, schemas.Unset] = schemas.unset,
        company_id: typing.Union[MetaOapg.properties.company_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransferProcessedEvent':
        return super().__new__(
            cls,
            *args,
            payment_type=payment_type,
            event_type=event_type,
            transfer_id=transfer_id,
            return_for_id=return_for_id,
            company_id=company_id,
            _configuration=_configuration,
            **kwargs,
        )

from brex_webhooks_python_sdk.model.payment_type import PaymentType
from brex_webhooks_python_sdk.model.webhook_event_type import WebhookEventType