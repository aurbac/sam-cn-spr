import json
import boto3
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):

    print("Hola")
    
    
    lines = []
    lines.append({'line': '5543514327', 'age': 28, 'location': 'Athens'})
    lines.append({'line': '5543514328', 'age': 28, 'location': 'Athens'})
    lines.append({'line': '5543514329', 'age': 28, 'location': 'Athens'})
    lines.append({'line': '5543514330', 'age': 28, 'location': 'Athens'})
    

    
    
    PROFILE_PRE_TABLE = os.environ['PROFILE_PRE_TABLE']
    PROFILE_POS_TABLE = os.environ['PROFILE_POS_TABLE']
    FLAGS_TABLE = os.environ['FLAGS_TABLE']

    return True

    '''
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
    '''