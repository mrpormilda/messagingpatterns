import pika
import time

# Wait a bit to ensure RabbitMQ is ready
time.sleep(5)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='hello')
message = "Hello from Dockerized Python App!"

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(f" [x] Sent '{message}'")
connection.close()
