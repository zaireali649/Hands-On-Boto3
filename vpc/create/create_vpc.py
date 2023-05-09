import boto3

vpc_cidr_block = '12.0.0.0/16'

ec2 = boto3.client('ec2')

vpc = ec2.create_vpc(CidrBlock=vpc_cidr_block)

print('VPC ID:', vpc['Vpc']['VpcId'])