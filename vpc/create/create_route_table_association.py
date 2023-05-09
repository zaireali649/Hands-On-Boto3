import boto3

# Specify subnet ID and route table ID
subnet_id = 'subnet-123456789'
route_table_id = 'rtb-123456789'

ec2 = boto3.client('ec2')

# Associate subnet with route table
association = ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=route_table_id)

# Print association ID
print('Association ID:', association['AssociationId'])
