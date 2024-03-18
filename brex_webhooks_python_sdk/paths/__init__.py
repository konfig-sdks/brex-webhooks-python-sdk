# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from brex_webhooks_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_WEBHOOKS = "/v1/webhooks"
    V1_WEBHOOKS_SECRETS = "/v1/webhooks/secrets"
    V1_WEBHOOKS_ID = "/v1/webhooks/{id}"
