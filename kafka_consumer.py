from confluent_kafka import Consumer, KafkaException

def consume_message():
    conf = {'bootstrap.servers': "localhost:9092", 'group.id': "test_group", 'auto.offset.reset': 'earliest'}
    consumer = Consumer(**conf)

    consumer.subscribe(['test_topic'])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    raise KafkaException(msg.error())
            print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_message()
