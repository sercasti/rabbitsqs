# Modernization: Move from RabbitMQ to Amazon SQS

This project is a sample on how to modernize your application, from using RabbitMQ (based on broker instances) to SQS (Serverless).

This example will use python Lambda samples, using python 3.8 and RabbitMQ 3.8.xx

## Pre-requisites

- Download this project (git clone)
- Open the AWS Console, Create a new Secret using Secrets manager:
  - Click "Other type of secrets".
  - In the Secret key/value, enter username for the first key and password for the second key. Enter any values you'd like to use. Password min chars: 12
  - For Secret name, enter ‘MQAccess’
  - Keep all other setting default
  - take note of the ARN for this new secret
- In the last line of the template.yaml file in this project, copy that ARN value.
- Run sam deploy --guided on your terminal, at the root of this project

## Usage

1. Open your AWS Console and find the Lambda service at: https://console.aws.amazon.com/lambda/home
1. Execute a test function on the MQProducer Lambda, consume the message with MQConsumer
1. Execute a test function on the SQSProducer Lambda, consume the message with SQSConsumer
1. Open your AWS Console and find the SNS service at: https://console.aws.amazon.com/sns/
1. Publish a message to the topic with a sample json body and the message attrib "coin" as "example_coin"
1. Publish a message to the topic with a sample json body and the message attrib "exchange_id" as "mynextexchange"
1. Check the SQS home to see how the routing between queues worked via filtering, as configured on template.yml with FilterPolicy on AWS::SNS::Subscription