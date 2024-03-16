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
s3_resource = boto3.resource('s3', config=config)


# The code you want to test
def get_object(bucket_name, result_prefix):
    s3_object = s3_resource.Object(bucket_name, result_prefix)
    response = s3_object.get()

    response_data = []
    while True:
        body_raw = response['Body'].read(8192)
        if not body_raw:
            break
        response_data.append(body_raw)

    data = b''.join(response_data).decode('utf-8-sig')
    print(data)