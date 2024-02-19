import json
import boto3
import os
from botocore.exceptions import ClientError

def makeObjectFromItem(record):
    result = {}
    for key, value in record.items():
        if 'S' in value:
            result[key] = str(value['S'])
        elif 'N' in value:
            result[key] = float(value['N'])
        elif 'BOOL' in value:
            result[key] = value["BOOL"]
        elif 'SS' in value:
            result[key] = value['SS']
        elif 'M' in value:
            result[key] = makeObjectFromItem(value['M'])
    return result

def lambda_handler(event, context):
    print(event)
    print(event['headers']['line'])
    
    PROFILE_PRE_TABLE = os.environ['PROFILE_PRE_TABLE']
    PROFILE_POS_TABLE = os.environ['PROFILE_POS_TABLE']
    
    try:
        db_client = boto3.client("dynamodb")
        response = db_client.get_item(
            TableName=PROFILE_PRE_TABLE,
            Key={
                'line': {
                    'S': event['headers']['line'],
                }
            }
        )
        print (response)
        if "Item" in response:
            return {
                "statusCode": 200,
                "body": json.dumps(makeObjectFromItem(response['Item'])),
            }
        else:
            return {
                "statusCode": 200,
                "body": "",
            }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": e,
        }
