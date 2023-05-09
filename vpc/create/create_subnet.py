import boto3

vpc_id = 'vpc-012345'
subnet_cidr_block = '12.0.1.0/24'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=subnet_cidr_block, VpcId=vpc_id)

print('Subnet ID:', subnet['Subnet']['SubnetId'])