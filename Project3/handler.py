import boto3
import face_recognition
import pickle
import os
import json
import logging
import csv
from boto3.dynamodb.conditions import Attr

S3_INPUT_BUCKET = "inputbucket"
S3_OUTPUT_BUCKET = "outputbucket"
PATH = "/tmp/"
table_name = 'Students-info-table'

endpoint = "http://localhost:8089"
ceph_access_key = 'DUK5D0BMR2LHPC8C1WXG'
ceph_secret_key = 'IJZZSPquWBsTM7GE1YwYmIG9ZWHkhXuItXa1HddM'


# Create S3 Client for uploading image and downloading the txt result file
s3_client = s3_client = boto3.client('s3', endpoint_url=endpoint, aws_access_key_id=ceph_access_key, aws_secret_access_key=ceph_secret_key)

# for dynamoDB
dynamo_client = boto3.resource('dynamodb')

table = dynamo_client.Table(table_name)


# uploads the result csv file to S3_OUTPUT_BUCKET
def upload_file_to_s3(csv_file, file_name):
    try:
        s3_client.upload_file(csv_file, S3_OUTPUT_BUCKET, file_name)
        logging.info("Output file uploaded to S3")
    except:
        print("Error while uploading output file to S3")


# this creates a file with file name and class name with comma separated
def create_result_file(file_name, name, year, major):
    output_filename = file_name.split('.')[0] + ".csv"
    with open(PATH + output_filename, "w", encoding='utf-8') as temp_file:
        result_writer = csv.writer(temp_file, delimiter=',')
        result_writer.writerow([name, major, year])
        temp_file.close()
    upload_file_to_s3(PATH + output_filename, output_filename)


# Function to read the 'encoding' file
def open_encoding(filename):
    file = open(filename, "rb")
    data = pickle.load(file)
    file.close()
    return data


# fetch the input file from S3_INPUT_BUCKET
def get_file_from_s3(file_name):
    print("Fetching result file from S3")
    s3_client.download_file(Bucket=S3_INPUT_BUCKET, Key=file_name, Filename=PATH + file_name)


def get_student_record_from_dynamo_db(student_name):
    try:
        response = table.scan(FilterExpression=Attr('name').eq(student_name))
        items = response.get('Items', [])
        if items:
            print("Match Found")
            # Assuming name is unique, so we return the first match
            return items[0]
    except Exception as e:
        print(f"Error encountered while querying the table: {e}")
    return None


def face_recognition_handler(event, context):
    filename = event['Records'][0]['s3']['object']['key']
    get_file_from_s3(filename)
    print("file fetched - ", filename)
    os.system("ffmpeg -i " + PATH + filename + " -r 1 " + str(PATH) + "image-%3d.jpeg")
    model = open_encoding("function/encoding")
    ff = face_recognition.load_image_file(PATH + "image-001.jpeg")
    ff_encoding = face_recognition.face_encodings(ff)[0]
    encoding_names = model['name']
    face_encodings = model['encoding']
    for index, face_encoding in enumerate(face_encodings):
        compare_result = face_recognition.compare_faces([face_encoding], ff_encoding)
        if compare_result[0]:
            student_record = get_student_record_from_dynamo_db(encoding_names[index])
            print(student_record)
            create_result_file(filename.split('.')[0], student_record['name'], student_record['year'], student_record['major'])
            break
    print("Face recognition task completed successfully")
