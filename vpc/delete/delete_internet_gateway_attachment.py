import boto3

internet_gateway_id = "igw-0f91ffb69d289cc87"
vpc_id = "vpc-0d5446c38f1a8bfb9"

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)