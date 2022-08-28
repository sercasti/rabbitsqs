import boto3
import os

sqs = boto3.client('sqs')

queue_url = os.environ['SQS_QUEUE_URL']

def lambda_handler(event, context):

    response = sqs.send_message(
      QueueUrl=queue_url,
      DelaySeconds=0,
      #see https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagegroupid-property.html
      MessageGroupId='myMessageGroup',
      MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'The Whistler'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'John Grisham'
        },
        'WeeksOn': {
            'DataType': 'Number',
            'StringValue': '6'
        }
      },
      MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
      )
    )

    print('MessageId:',response['MessageId'])