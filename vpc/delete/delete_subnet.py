import boto3

subnet_id = 'subnet-012345'

# Create EC2 client
ec2 = boto3.client('ec2')

ec2.delete_subnet(SubnetId=subnet_id)