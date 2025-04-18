import pika
import time

time.sleep(5)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_topic', exchange_type='topic')

# Create a queue and bind it to topics starting with 'info'
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs_topic', queue=queue_name, routing_key='info.*')

def callback(ch, method, properties, body):
    print(f"[Consumer1] Received '{body.decode()}' with key '{method.routing_key}'")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print('[Consumer1] Waiting for messages...')
channel.start_consuming()
