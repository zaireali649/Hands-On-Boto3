import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='zali-boto3-05012023'
)

print(response)