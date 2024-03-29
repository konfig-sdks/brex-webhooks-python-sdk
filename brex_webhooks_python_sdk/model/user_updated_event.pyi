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


class UserUpdatedEvent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The webhook will be sent when a user is updated.
    """


    class MetaOapg:
        required = {
            "event_type",
            "company_id",
            "user_id",
            "updated_attributes",
        }
        
        class properties:
        
            @staticmethod
            def event_type() -> typing.Type['WebhookEventType']:
                return WebhookEventType
            user_id = schemas.StrSchema
            company_id = schemas.StrSchema
            
            
            class updated_attributes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['UserAttributes']:
                        return UserAttributes
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['UserAttributes'], typing.List['UserAttributes']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'updated_attributes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'UserAttributes':
                    return super().__getitem__(i)
            __annotations__ = {
                "event_type": event_type,
                "user_id": user_id,
                "company_id": company_id,
                "updated_attributes": updated_attributes,
            }
    
    event_type: 'WebhookEventType'
    company_id: MetaOapg.properties.company_id
    user_id: MetaOapg.properties.user_id
    updated_attributes: MetaOapg.properties.updated_attributes
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> 'WebhookEventType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_attributes"]) -> MetaOapg.properties.updated_attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["event_type", "user_id", "company_id", "updated_attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> 'WebhookEventType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_attributes"]) -> MetaOapg.properties.updated_attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["event_type", "user_id", "company_id", "updated_attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        event_type: 'WebhookEventType',
        company_id: typing.Union[MetaOapg.properties.company_id, str, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, ],
        updated_attributes: typing.Union[MetaOapg.properties.updated_attributes, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserUpdatedEvent':
        return super().__new__(
            cls,
            *args,
            event_type=event_type,
            company_id=company_id,
            user_id=user_id,
            updated_attributes=updated_attributes,
            _configuration=_configuration,
            **kwargs,
        )

from brex_webhooks_python_sdk.model.user_attributes import UserAttributes
from brex_webhooks_python_sdk.model.webhook_event_type import WebhookEventType
