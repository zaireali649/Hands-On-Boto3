import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify route table ID and destination CIDR block
route_table_id = 'rtb-123456789'
destination_cidr_block = '0.0.0.0/0'

# Delete route
response = ec2.delete_route(
    DestinationCidrBlock=destination_cidr_block,
    RouteTableId=route_table_id
)

# Print response
print(response)
