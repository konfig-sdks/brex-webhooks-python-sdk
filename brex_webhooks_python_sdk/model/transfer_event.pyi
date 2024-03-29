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


class TransferEvent(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "payment_type",
            "company_id",
        }
        
        @staticmethod
        def discriminator():
            return {
                'event_type': {
                    'TRANSFER_FAILED': TransferFailedEvent,
                    'TRANSFER_PROCESSED': TransferProcessedEvent,
                    'TransferFailedEvent': TransferFailedEvent,
                    'TransferProcessedEvent': TransferProcessedEvent,
                }
            }
        
        class properties:
            company_id = schemas.StrSchema
        
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
            __annotations__ = {
                "company_id": company_id,
                "payment_type": payment_type,
                "return_for_id": return_for_id,
            }
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                TransferProcessedEvent,
                TransferFailedEvent,
            ]

    
    payment_type: 'PaymentType'
    company_id: MetaOapg.properties.company_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_type"]) -> 'PaymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["return_for_id"]) -> MetaOapg.properties.return_for_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["company_id", "payment_type", "return_for_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_type"]) -> 'PaymentType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["return_for_id"]) -> typing.Union[MetaOapg.properties.return_for_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company_id", "payment_type", "return_for_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payment_type: 'PaymentType',
        company_id: typing.Union[MetaOapg.properties.company_id, str, ],
        return_for_id: typing.Union[MetaOapg.properties.return_for_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransferEvent':
        return super().__new__(
            cls,
            *args,
            payment_type=payment_type,
            company_id=company_id,
            return_for_id=return_for_id,
            _configuration=_configuration,
            **kwargs,
        )

from brex_webhooks_python_sdk.model.payment_type import PaymentType
from brex_webhooks_python_sdk.model.transfer_failed_event import TransferFailedEvent
from brex_webhooks_python_sdk.model.transfer_processed_event import TransferProcessedEvent
