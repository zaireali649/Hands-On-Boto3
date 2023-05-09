import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify route table ID and destination CIDR block
vpc_id = 'vpc-01234'
internet_gateway_id = 'igw-123456789'

ec2.detach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)