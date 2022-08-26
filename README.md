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