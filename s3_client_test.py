import boto3
from botocore.config import Config
from moto import mock_aws

from s3_client import list_buckets


region = 'ap-northeast-1'
config = Config(
    region_name=region,
    retries={
        'mode': 'standard',
        'max_attempts': 3
    }
)
# boto3 to be replaced by mock
s3_client = boto3.client('s3', config=config)


# Just apply the @mock_aws decorator to the function you want to mock
@mock_aws
def test_list_buckets():
    bucket_name_list = ['s3_bucket' + str(i) for i in range(1, 6, 1)]

    # To create a virtual S3 bucket locally
    for bucket in bucket_name_list:
        s3_client.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )

    # Call the code you want to test
    list_buckets()


# When debugging, execute the mock code
if __name__ == '__main__':
    test_list_buckets()