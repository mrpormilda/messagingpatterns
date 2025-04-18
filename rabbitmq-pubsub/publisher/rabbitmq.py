import pika

def publish_message(routing_key: str, message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs_topic', exchange_type='topic')
    channel.basic_publish(
        exchange='logs_topic',
        routing_key=routing_key,
        body=message
    )
    print(f"[x] Published '{message}' with key '{routing_key}'")
    connection.close()
