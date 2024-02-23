import boto3
import botocore

# Ceph Object Gateway credentials
s3_endpoint = "http://localhost:8089"
s3_access_key = 'DUK5D0BMR2LHPC8C1WXG'
s3_secret_key = 'IJZZSPquWBsTM7GE1YwYmIG9ZWHkhXuItXa1HddM'
s3_bucket_name = 'outputbucket'

def download_file_from_ceph(file_name, local_destination):
    s3_client = boto3.client('s3', endpoint_url=s3_endpoint, aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_key)

    try:
        s3_client.download_file(s3_bucket_name, file_name, local_destination)
        print(f"File '{file_name}' downloaded successfully to '{local_destination}'.")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print(f"File '{file_name}' not found in the bucket.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Take user input for file name
    file_name = input("Enter the name of the file to download: ")

    # Specify local destination for the downloaded file
    local_destination = f"./{file_name}"

    # Download the requested file from the Ceph bucket
    download_file_from_ceph(file_name, local_destination)

