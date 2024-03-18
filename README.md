<div align="left">

[![Visit Brex](./header.png)](https://brex.com)

# Brex<a id="brex"></a>


Brex uses webhooks to send real-time notifications when events happen in the accounts that you manage.
Use webhook subscriptions to subscribe to different webhook events.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`brexwebhooks.webhook_subscriptions.get_details`](#brexwebhookswebhook_subscriptionsget_details)
  * [`brexwebhooks.webhook_subscriptions.list`](#brexwebhookswebhook_subscriptionslist)
  * [`brexwebhooks.webhook_subscriptions.list_secrets`](#brexwebhookswebhook_subscriptionslist_secrets)
  * [`brexwebhooks.webhook_subscriptions.register_endpoint`](#brexwebhookswebhook_subscriptionsregister_endpoint)
  * [`brexwebhooks.webhook_subscriptions.unregister_webhook`](#brexwebhookswebhook_subscriptionsunregister_webhook)
  * [`brexwebhooks.webhook_subscriptions.update_webhook`](#brexwebhookswebhook_subscriptionsupdate_webhook)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Brex&serviceName=Webhooks&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from brex_webhooks_python_sdk import BrexWebhooks, ApiException

brexwebhooks = BrexWebhooks(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Get Webhook
    get_details_response = brexwebhooks.webhook_subscriptions.get_details(
        id="id_example",
    )
    print(get_details_response)
except ApiException as e:
    print("Exception when calling WebhookSubscriptionsApi.get_details: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from brex_webhooks_python_sdk import BrexWebhooks, ApiException

brexwebhooks = BrexWebhooks(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Get Webhook
        get_details_response = await brexwebhooks.webhook_subscriptions.aget_details(
            id="id_example",
        )
        print(get_details_response)
    except ApiException as e:
        print("Exception when calling WebhookSubscriptionsApi.get_details: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from brex_webhooks_python_sdk import BrexWebhooks, ApiException

brexwebhooks = BrexWebhooks(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Get Webhook
    get_details_response = brexwebhooks.webhook_subscriptions.raw.get_details(
        id="id_example",
    )
    pprint(get_details_response.body)
    pprint(get_details_response.body["id"])
    pprint(get_details_response.body["url"])
    pprint(get_details_response.body["event_types"])
    pprint(get_details_response.body["status"])
    pprint(get_details_response.headers)
    pprint(get_details_response.status)
    pprint(get_details_response.round_trip_time)
except ApiException as e:
    print("Exception when calling WebhookSubscriptionsApi.get_details: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `brexwebhooks.webhook_subscriptions.get_details`<a id="brexwebhookswebhook_subscriptionsget_details"></a>

Get details of a webhook

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = brexwebhooks.webhook_subscriptions.get_details(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./brex_webhooks_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhooks/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexwebhooks.webhook_subscriptions.list`<a id="brexwebhookswebhook_subscriptionslist"></a>

List the webhooks you have registered

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = brexwebhooks.webhook_subscriptions.list(
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PageWebhookSubscription`](./brex_webhooks_python_sdk/pydantic/page_webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexwebhooks.webhook_subscriptions.list_secrets`<a id="brexwebhookswebhook_subscriptionslist_secrets"></a>


This endpoint returns a set of webhook signing secrets used to validate the webhook.
Usually only one key will be returned in the response. After key rotation, this endpoint will return two keys:
the new key, and the key that will be revoked soon. There will also be two signatures in the 'Webhook-Signature' request header.
Your application should use all keys available to validate the webhook request. If validation passes for any
of the keys returned, the webhook payload is valid.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_secrets_response = brexwebhooks.webhook_subscriptions.list_secrets()
```

#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscriptionsListSecretsResponse`](./brex_webhooks_python_sdk/pydantic/webhook_subscriptions_list_secrets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhooks/secrets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexwebhooks.webhook_subscriptions.register_endpoint`<a id="brexwebhookswebhook_subscriptionsregister_endpoint"></a>

Register an endpoint to start receiving selected webhook events

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_endpoint_response = brexwebhooks.webhook_subscriptions.register_endpoint(
    url="string_example",
    event_types=[
        "string_example"
    ],
    idempotency_key="Idempotency-Key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

##### event_types: List[[`WebhookEventType`](./brex_webhooks_python_sdk/type/webhook_event_type.py)]<a id="event_types-listwebhookeventtypebrex_webhooks_python_sdktypewebhook_event_typepy"></a>

The Brex API sends webhooks for the events listed below. For more details, see the [webhook guide](https://developer.brex.com/openapi/webhooks_api/) and [webhook events API reference](https://developer.brex.com/openapi/webhooks_api/).

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateWebhookSubscriptionRequest`](./brex_webhooks_python_sdk/type/create_webhook_subscription_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./brex_webhooks_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexwebhooks.webhook_subscriptions.unregister_webhook`<a id="brexwebhookswebhook_subscriptionsunregister_webhook"></a>

Unregister a webhook if you want to stop receiving webhook events

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
brexwebhooks.webhook_subscriptions.unregister_webhook(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhooks/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexwebhooks.webhook_subscriptions.update_webhook`<a id="brexwebhookswebhook_subscriptionsupdate_webhook"></a>

Update a webhook.
You can update the endpoint url, event types that the endpoint receives, or temporarily deactivate the webhook.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_response = brexwebhooks.webhook_subscriptions.update_webhook(
    url="string_example",
    event_types=[
        "string_example"
    ],
    status="ACTIVE",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

##### event_types: List[[`WebhookEventType`](./brex_webhooks_python_sdk/type/webhook_event_type.py)]<a id="event_types-listwebhookeventtypebrex_webhooks_python_sdktypewebhook_event_typepy"></a>

##### status: [`UpdateWebhookSubscriptionStatus`](./brex_webhooks_python_sdk/type/update_webhook_subscription_status.py)<a id="status-updatewebhooksubscriptionstatusbrex_webhooks_python_sdktypeupdate_webhook_subscription_statuspy"></a>

##### id: `str`<a id="id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateWebhookSubscriptionRequest`](./brex_webhooks_python_sdk/type/update_webhook_subscription_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhookSubscription`](./brex_webhooks_python_sdk/pydantic/webhook_subscription.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/webhooks/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
