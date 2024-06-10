import pika

def send_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='test_queue')

    channel.basic_publish(exchange='', routing_key='test_queue', body=message)
    print(f"Sent '{message}'")

    connection.close()

if __name__ == "__main__":
    send_message('Hello, RabbitMQ!')
