import typing_extensions

from brex_webhooks_python_sdk.apis.tags import TagValues
from brex_webhooks_python_sdk.apis.tags.webhook_subscriptions_api import WebhookSubscriptionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WEBHOOK_SUBSCRIPTIONS: WebhookSubscriptionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WEBHOOK_SUBSCRIPTIONS: WebhookSubscriptionsApi,
    }
)
