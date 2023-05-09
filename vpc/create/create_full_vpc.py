import boto3

# Define VPC CIDR block, public subnet CIDR block, and private subnet CIDR block
vpc_cidr_block = '11.0.0.0/16'
public_subnet_cidr_block = '11.0.1.0/24'
private_subnet_cidr_block = '11.0.2.0/24'

# Create EC2 client
ec2 = boto3.client('ec2')

# Create VPC
vpc = ec2.create_vpc(CidrBlock=vpc_cidr_block)

# Enable DNS hostname for the VPC
ec2.modify_vpc_attribute(VpcId=vpc['Vpc']['VpcId'], EnableDnsHostnames={'Value': True})

# Create internet gateway
internet_gateway = ec2.create_internet_gateway()

# Attach internet gateway to VPC
ec2.attach_internet_gateway(InternetGatewayId=internet_gateway['InternetGateway']['InternetGatewayId'], VpcId=vpc['Vpc']['VpcId'])

# Create public subnet
public_subnet = ec2.create_subnet(CidrBlock=public_subnet_cidr_block, VpcId=vpc['Vpc']['VpcId'])

# Create private subnet
private_subnet = ec2.create_subnet(CidrBlock=private_subnet_cidr_block, VpcId=vpc['Vpc']['VpcId'])

# Create public route table
public_route_table = ec2.create_route_table(VpcId=vpc['Vpc']['VpcId'])
ec2.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internet_gateway['InternetGateway']['InternetGatewayId'], RouteTableId=public_route_table['RouteTable']['RouteTableId'])
ec2.associate_route_table(RouteTableId=public_route_table['RouteTable']['RouteTableId'], SubnetId=public_subnet['Subnet']['SubnetId'])

# Create private route table
private_route_table = ec2.create_route_table(VpcId=vpc['Vpc']['VpcId'])
ec2.associate_route_table(RouteTableId=private_route_table['RouteTable']['RouteTableId'], SubnetId=private_subnet['Subnet']['SubnetId'])

# Print VPC and subnet IDs
print('VPC ID:', vpc['Vpc']['VpcId'])
print('Public Subnet ID:', public_subnet['Subnet']['SubnetId'])
print('Private Subnet ID:', private_subnet['Subnet']['SubnetId'])
