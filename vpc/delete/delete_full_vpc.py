import boto3

# Define VPC ID, public subnet ID, and private subnet ID
vpc_id = 'vpc-04c957c85a4e74b5c'
public_subnet_id = 'subnet-0e545b89a48f5d999'
private_subnet_id = 'subnet-088323f96bb6627c8'

# Create EC2 client
ec2 = boto3.client('ec2')

# Delete NAT gateway
try:
    nat_gateway_id = ec2.describe_nat_gateways(Filters=[{'Name': 'subnet-id', 'Values': [public_subnet_id]}])['NatGateways'][0]['NatGatewayId']
    ec2.delete_nat_gateway(NatGatewayId=nat_gateway_id)
except:
    pass

# Delete public subnet route table association
public_route_table_id = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'association.subnet-id', 'Values': [public_subnet_id]}])['RouteTables'][0]['RouteTableId']
ec2.disassociate_route_table(AssociationId=ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'association.subnet-id', 'Values': [public_subnet_id]}])['RouteTables'][0]['Associations'][0]['RouteTableAssociationId'])
ec2.delete_route_table(RouteTableId=public_route_table_id)


# Delete private subnet route table association
private_route_table_id = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'association.subnet-id', 'Values': [private_subnet_id]}])['RouteTables'][0]['RouteTableId']
ec2.disassociate_route_table(AssociationId=ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}, {'Name': 'association.subnet-id', 'Values': [private_subnet_id]}])['RouteTables'][0]['Associations'][0]['RouteTableAssociationId'])
ec2.delete_route_table(RouteTableId=private_route_table_id)


# Detach and delete internet gateway
internet_gateway_id = ec2.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}])['InternetGateways'][0]['InternetGatewayId']
ec2.detach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)
ec2.delete_internet_gateway(InternetGatewayId=internet_gateway_id)


# Delete subnets
ec2.delete_subnet(SubnetId=public_subnet_id)
ec2.delete_subnet(SubnetId=private_subnet_id)


# Delete VPC
ec2.delete_vpc(VpcId=vpc_id)
