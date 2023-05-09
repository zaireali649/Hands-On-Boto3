import boto3

vpc_id = 'vpc-012345'

# Create EC2 client
ec2 = boto3.client('ec2')

ec2.delete_vpc(VpcId=vpc_id)