import boto3

vpc_id = "vpc-0d5446c38f1a8bfb9"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)