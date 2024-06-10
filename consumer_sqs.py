import boto3

def consume_message():
    sqs = boto3.client('sqs', region_name='us-east-1')

    queue_url = 'https://sqs.us-east-1.amazonaws.com/YOUR_ACCOUNT_ID/YOUR_QUEUE_NAME'

    while True:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10
        )

        messages = response.get('Messages', [])
        if not messages:
            continue

        for message in messages:
            print(f"Received message: {message['Body']}")

            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

if __name__ == "__main__":
    consume_message()
