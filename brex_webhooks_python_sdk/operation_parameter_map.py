operation_parameter_map = {
    '/v1/webhooks/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/webhooks-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/webhooks/secrets-GET': {
        'parameters': [
        ]
    },
    '/v1/webhooks-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'event_types'
            },
            {
                'name': 'Idempotency-Key'
            },
        ]
    },
    '/v1/webhooks/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/webhooks/{id}-PUT': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'event_types'
            },
            {
                'name': 'status'
            },
            {
                'name': 'id'
            },
        ]
    },
};