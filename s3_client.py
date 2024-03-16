import boto3
from botocore.config import Config


region = 'ap-northeast-1'
config = Config(
    region_name=region,
    retries={
        'mode': 'standard',
        'max_attempts': 3
    }
)
# Replaced with a mock in the test function calling it
s3_client = boto3.client('s3', config=config)


# The code you want to test
def list_buckets():

    response = s3_client.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    print(buckets)