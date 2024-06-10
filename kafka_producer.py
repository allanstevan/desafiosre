from confluent_kafka import Producer

def send_message(message):
    conf = {'bootstrap.servers': "localhost:9092"}
    producer = Producer(**conf)

    def delivery_report(err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    producer.produce('test_topic', key='key', value=message, callback=delivery_report)
    producer.flush()

if __name__ == "__main__":
    send_message('Hello, Kafka!')
