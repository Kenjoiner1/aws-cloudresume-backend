import json
import boto3 # type: ignore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCount')  # Replace with your actual table name

def lambda_handler(event, context):
    try:
        response = table.update_item(
            Key={'id': 'counter'},
            UpdateExpression='ADD visit_count :incr',
            ExpressionAttributeValues={':incr': 1},
            ReturnValues='UPDATED_NEW'
        )

        new_count = response['Attributes']['visit_count']

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'visit_count': int(new_count)})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
