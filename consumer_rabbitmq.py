import pika

def callback(ch, method, properties, body):
    print(f"Received '{body}'")

def consume_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='test_queue')

    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_message()
