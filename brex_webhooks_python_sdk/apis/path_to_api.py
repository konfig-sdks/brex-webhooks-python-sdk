import typing_extensions

from brex_webhooks_python_sdk.paths import PathValues
from brex_webhooks_python_sdk.apis.paths.v1_webhooks import V1Webhooks
from brex_webhooks_python_sdk.apis.paths.v1_webhooks_secrets import V1WebhooksSecrets
from brex_webhooks_python_sdk.apis.paths.v1_webhooks_id import V1WebhooksId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_WEBHOOKS: V1Webhooks,
        PathValues.V1_WEBHOOKS_SECRETS: V1WebhooksSecrets,
        PathValues.V1_WEBHOOKS_ID: V1WebhooksId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_WEBHOOKS: V1Webhooks,
        PathValues.V1_WEBHOOKS_SECRETS: V1WebhooksSecrets,
        PathValues.V1_WEBHOOKS_ID: V1WebhooksId,
    }
)
