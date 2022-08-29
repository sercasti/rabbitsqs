import boto3
import os

# Yes, you can trigger a Lambda from SQS directly, but this code is meant to 
# represent a process running on a virtual machine for modernization purposes

sqs = boto3.client('sqs')

queue_url = os.environ['SQS_QUEUE_URL']

def lambda_handler(event, context):

    # Receive message from SQS queue
    # see https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.receive_message
    response = sqs.receive_message(
      QueueUrl=queue_url,
      #AWS attributes (MessageGroupId, SequenceNumber, SentTimestamp, MessageDeduplicationId)
      AttributeNames=[
        'SentTimestamp'
      ],
      MaxNumberOfMessages=1,
      MessageAttributeNames=[
        'All'
      ],
      #see https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html
      VisibilityTimeout=60, #time SQS prevents other consumers from receiving the message
      #see https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html
      WaitTimeSeconds=0 #Short polling
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue (ack)
    # see https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html#configuring-visibility-timeout
    sqs.delete_message(
      QueueUrl=queue_url,
      ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)