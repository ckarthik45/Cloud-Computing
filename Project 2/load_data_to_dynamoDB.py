import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', aws_access_key_id='AKIAZIVS4KWRZ4IU7Z6P', aws_secret_access_key='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')

# tables = list(dynamodb.tables.all())
# print(tables)
table = dynamodb.Table('Students-info-table')


def find():
    response = table.query(
        KeyConditionExpression=Key('name').eq('floki')
    )

    for i in response['Items']:
        print(i)


find()


# def insert():
#     student_data = json.load(open('student_data.json'))
#     for item in student_data:
#         response = table.put_item(
#             Item=item
#         )
#         print(response)
#
#
# insert()
