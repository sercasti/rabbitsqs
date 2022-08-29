# Modernization: Move from RabbitMQ to Amazon SQS

This project is a sample on how to modernize your application, from using RabbitMQ (based on broker instances) to SQS (Serverless).

This example will use python Lambda samples, using python 3.8 and RabbitMQ 3.8.xx

## Pre-requisites

- Download this project (git clone)
- Open the AWS Console, Create a new Secret using Secrets manager:
  - Click "Other type of secrets".
  - In the Secret key/value, enter username for the first key and password for the second key. Enter any values you'd like to use. Password min chars: 12
  - For Secret name, enter ‘MQAccess’
  - Keep all other setting default.
  - Make sure secret name was saved as ‘MQAccess’

    ![secret](/assets/images/0.secret.png)
- Make sure your AWS credentials are set on your terminal session for the right AWS account
- Run sam deploy --guided on your terminal, at the root of this project. Just hit 'Enter' for every prompt. This will create all the resources on your AWS account via CloudFormation.

## Usage

1. Open your AWS Console and find the Lambda service at: https://console.aws.amazon.com/lambda/home
 ![Lambdas](/assets/images/1.lambda%20functions.png)
1. Execute a test function on the MQProducer Lambda, consume the message with MQConsumer
 ![ConsumeMQ](/assets/images/2.consume%20mq.png)
1. Execute a test function on the SQSProducer Lambda, consume the message with SQSConsumer
 ![producesqs](/assets/images/3.produce%20message.png)
 ![consumesqs](/assets/images/4.consume%20message.png)
1. Observe the queues created for exchanges and coins:
 ![allqueues](/assets/images/5.all%20queues.png)
1. Open your AWS Console and find the SNS service at: https://console.aws.amazon.com/sns/
 ![sns](/assets/images/6.topic%20subscriptions.png)
1. Publish a message to the topic with a sample json body and the message attrib "coin" as "example_coin"
 ![publishsns](/assets/images/7.publish%20message.png)
1. Publish a message to the topic with a sample json body and the message attrib "exchange_id" as "mynextexchange"
1. Check the SQS home to see how the routing between queues worked via filtering, as configured on template.yml with FilterPolicy on AWS::SNS::Subscription
 ![sns](/assets/images/8.sent%20Messages.png)
1. You can do any combination of message attributes to do dynamic routing/filtering
 ![combine](/assets/images/9.combine.png)
1. poll for messages on each SQS queue to get the message
 ![poll](/assets/images/10.received%20sqs.png)
1. check the message details to confirm routing worked as expected
 ![read](/assets/images/11.view%20message.png)