from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import logging
from botocore.exceptions import ClientError
import os

app = Flask(__name__)
CORS(app)

# Load AWS credentials from environment variables
s3 = boto3.client(
    's3',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def upload_file(file, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file: File-like object to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    try:
        s3.upload_fileobj(file, bucket, object_name or file.filename)
        return True
    except ClientError as e:
        logging.error(e)
        return False

def get_bucket_name_from_file():
    """Read the bucket name from s3list.txt"""
    try:
        with open('s3list.txt', 'r') as file:
            bucket_name = file.readline().strip()
        return bucket_name
    except IOError as e:
        logging.error(f"Error reading s3list.txt: {e}")
        return None

@app.route('/upload', methods=['POST'])
def upload():
    bucket = get_bucket_name_from_file()
    if not bucket:
        return jsonify({'error': 'Could not retrieve bucket name'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if upload_file(file, bucket):
        return jsonify({'message': 'File uploaded successfully!'}), 200
    else:
        return jsonify({'error': 'Failed to upload file'}), 500

if __name__ == '__main__':
    app.run(debug=True)
