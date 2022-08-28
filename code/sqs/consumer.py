import boto3
import os

# Yes, you can trigger a Lambda from SQS directly, but this code is meant to 
# represent a process running on a virtual machine for modernization purposes

sqs = boto3.client('sqs')

queue_url = os.environ['SQS_QUEUE_URL']

def lambda_handler(event, context):

    # Receive message from SQS queue
    response = sqs.receive_message(
      QueueUrl=queue_url,
      AttributeNames=[
        'SentTimestamp'
      ],
      MaxNumberOfMessages=1,
      MessageAttributeNames=[
        'All'
      ],
      VisibilityTimeout=60,
      WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue
    sqs.delete_message(
      QueueUrl=queue_url,
      ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)