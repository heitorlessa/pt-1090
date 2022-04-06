import json
import os

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.utilities.idempotency import (
    DynamoDBPersistenceLayer, idempotent)

persistence_layer = DynamoDBPersistenceLayer(table_name=os.getenv("IDEMPOTENCY_TABLE"))

@idempotent(persistence_store=persistence_layer)

def lambda_handler(event: dict, context: LambdaContext):
    """Mutates and return event to reproduce issue #1090"""
    event.popitem()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
