import boto3
import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

s3 = boto3.client(
    's3',
    region_name=os.getenv('AWS_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """
    try:
        if region is None:
            s3.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name,
                             CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def bucket_name_exists(bucket_name, file_path='s3list.txt'):
    """Check if the bucket name already exists in the file.

    :param bucket_name: Bucket name to check
    :param file_path: File to check for existing bucket names
    :return: True if bucket name exists in the file, else False
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_buckets = file.read().splitlines()
            return bucket_name in existing_buckets
    return False

def save_bucket_name(bucket_name, file_path='s3list.txt'):
    """Save the bucket name to the file.

    :param bucket_name: Bucket name to save
    :param file_path: File to save the bucket name
    """
    with open(file_path, 'a') as file:
        file.write(bucket_name + '\n')

# Generate current date formatted as monthdayyear
current_time = datetime.now().strftime("%m%d%Y")

# Generate bucket name
bucket_name = f"s3bucket{current_time}"

# File path for bucket names
file_path = 's3list.txt'

# Check if the bucket name already exists
if bucket_name_exists(bucket_name, file_path):
    print(f"Bucket {bucket_name} already exists in the file.")
else:
    # Create the bucket
    region = os.getenv('AWS_REGION')
    success = create_bucket(bucket_name, region)

    if success:
        print(f"Bucket {bucket_name} created successfully!")
        save_bucket_name(bucket_name, file_path)
    else:
        print(f"Failed to create bucket {bucket_name}.")
