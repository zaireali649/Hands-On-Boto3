import boto3

# Specify VPC ID
vpc_id = 'vpc-123456789'

ec2 = boto3.client('ec2')

# Create route table
route_table = ec2.create_route_table(VpcId=vpc_id)

# Print route table ID
print('Route table ID:', route_table['RouteTable']['RouteTableId'])
