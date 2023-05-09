import boto3

vpc_id = 'vpc-012345'
internet_gateway_id = 'igw-123456789'

ec2 = boto3.client('ec2')

# Create internet gateway
ec2.attach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)
