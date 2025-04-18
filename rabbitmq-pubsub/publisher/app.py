import pika
import time

time.sleep(5)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declare a topic exchange
channel.exchange_declare(exchange='logs_topic', exchange_type='topic')

routing_keys = ['info.weather', 'warn.system', 'error.security']

for key in routing_keys:
    message = f"Message with key '{key}'"
    channel.basic_publish(
        exchange='logs_topic',
        routing_key=key,
        body=message
    )
    print(f" [x] Sent {message}")

connection.close()
