import json

from .demo_dynamo_store import save_demo_data


def create_base_response(body: object, status: int):
    return {
        "statusCode": status,
        "body": json.dumps(body),
    }


def run_post_event(event_body):

    save_demo_data(json.loads(event_body)["userName"])

    return create_base_response({"message": "data stored"}, 200)


def run_get_event(eventBody):
    return create_base_response({"message": "hi"}, 200)


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format # nopep8

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    if event["httpMethod"] == "POST":
        return run_post_event(event["body"])
    elif event["httpMethod"] == "GET":
        return run_get_event(event["body"])
    else:
        return {
            "statusCode": 500,
            "errorType": "MethodNotSupported"
        }
