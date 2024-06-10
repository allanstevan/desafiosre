import boto3

def send_message(message):
    sqs = boto3.client('sqs', region_name='us-east-1')

    queue_url = 'https://sqs.us-east-1.amazonaws.com/YOUR_ACCOUNT_ID/YOUR_QUEUE_NAME'

    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )

    print(f"Sent message ID: {response['MessageId']}")

if __name__ == "__main__":
    send_message('Hello, SQS!')
