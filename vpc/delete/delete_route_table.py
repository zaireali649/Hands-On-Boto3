import boto3

route_table_id = 'rt-012345'

# Create EC2 client
ec2 = boto3.client('ec2')

ec2.delete_route_table(RouteTableId=route_table_id)