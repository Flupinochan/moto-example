import boto3
from botocore.config import Config
from moto import mock_aws

from s3_resource import get_object


region = 'ap-northeast-1'
config = Config(
    region_name=region,
    retries={
        'mode': 'standard',
        'max_attempts': 3
    }
)
# boto3 to be replaced by mock
s3_resource = boto3.resource('s3', config=config)


# Just apply the @mock_aws decorator to the function you want to mock
@mock_aws
def test_get_object():
    bucket_name = 's3_bucket'
    result_prefix = 's3_prefix'
    data = b'Hello, moto'

    # To create a virtual S3 bucket locally
    s3_bucket = s3_resource.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
    )
    s3_bucket.put_object(Key=result_prefix, Body=data)

    # Call the code you want to test
    get_object(bucket_name, result_prefix)


# When debugging, execute the mock code
if __name__ == '__main__':
    test_get_object()