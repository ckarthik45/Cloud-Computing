import boto3
import requests

# Ceph Object Gateway credentials
s3_endpoint = 'http://localhost:8089'
s3_access_key = 'DUK5D0BMR2LHPC8C1WXG'
s3_secret_key = 'IJZZSPquWBsTM7GE1YwYmIG9ZWHkhXuItXa1HddM'
s3_bucket_name = 'inputbucket'

# OpenFaaS function details
openfaas_gateway = "http://localhost:8080"
openfaas_function_name = 'project3'

def trigger_openfaas_function(event):
    # Trigger OpenFaaS function
    url = f"{openfaas_gateway}/async-function/{openfaas_function_name}"
    response = requests.post(url, json=event)
    print(f"OpenFaaS function triggered with status code: {response.status_code}")

def monitor_ceph_bucket():
    # Set up S3 client
    s3_client = boto3.client('s3', endpoint_url=s3_endpoint, aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_key)

    # Start monitoring the bucket
    print(f"Monitoring bucket '{s3_bucket_name}' for new object uploads...")
    bucket_notifications = s3_client.get_bucket_notification_configuration(Bucket=s3_bucket_name)

    # Loop indefinitely to continuously monitor the bucket
    while True:
        try:
            events = s3_client.get_bucket_notification(Bucket=s3_bucket_name)
            for record in events['Records']:
                # Example: Trigger OpenFaaS function with the object key as the event payload
                event_payload = {'object_key': record['s3']['object']['key']}
                trigger_openfaas_function(event_payload)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    monitor_ceph_bucket()

