import pika   #Python AMQP Library

import os
import ssl
import datetime

# get Environment Variables
RABBIT_HOST = os.environ['mqhost']
RABBIT_USER = os.environ['mquser']
RABBIT_PWD = os.environ['mqpass']

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')
ssl_options = pika.SSLOptions(context=ssl_context)

credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PWD)
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
parameters = pika.ConnectionParameters(credentials=credentials, host=RABBIT_HOST, ssl_options=ssl_options)  

# parameters and credentials ready to support calls to RabbitMQ
connection = pika.BlockingConnection(parameters)  #Establishes TCP Connection with RabbitMQ
channel = connection.channel()  #Establishes logical channel within Connection
channel.queue_declare(queue='myQueue')

def lambda_handler(event, context):
    #Send Message
    channel.basic_publish(exchange='', routing_key='', body='Howdy RabbitMQ, Lambda Here!! ' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") + ' UTC') 