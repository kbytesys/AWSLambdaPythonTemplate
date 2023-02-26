import os
import boto3
from boto3.dynamodb import conditions

DYNAMO_TABLE_NAME = "DYNAMO_TABLE_NAME"


def get_demo_dynamo_table():
    dynamodb_resource = boto3.resource("dynamodb")
    return dynamodb_resource.Table(os.environ[DYNAMO_TABLE_NAME])


def get_demo_data(demo_key: str) -> list:
    table = get_demo_dynamo_table()

    response = table.query(
        KeyConditionExpression=conditions.Key("PK").eq(f"{demo_key}")
    )

    return response["Items"]


def save_demo_data(demo_key: str):
    demo_record = dict()
    demo_record["PK"] = f"{demo_key}"

    table = get_demo_dynamo_table()
    table.put_item(Item=demo_record)
