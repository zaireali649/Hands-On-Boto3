import boto3

subnet_id = "subnet-0bd7e74203e0f1a09"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)