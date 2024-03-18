from brex_webhooks_python_sdk.paths.v1_webhooks_id.get import ApiForget
from brex_webhooks_python_sdk.paths.v1_webhooks_id.put import ApiForput
from brex_webhooks_python_sdk.paths.v1_webhooks_id.delete import ApiFordelete


class V1WebhooksId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
