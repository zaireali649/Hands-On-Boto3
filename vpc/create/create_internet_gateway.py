import boto3

ec2 = boto3.client('ec2')

# Create internet gateway
internet_gateway = ec2.create_internet_gateway()

# Print internet gateway ID
print('Internet gateway ID:', internet_gateway['InternetGateway']['InternetGatewayId'])
