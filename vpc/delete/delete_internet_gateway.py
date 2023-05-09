import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

internet_gateway_id = 'igw-123456789'

ec2.delete_internet_gateway(InternetGatewayId=internet_gateway_id)