import boto3

route_table_id = 'rt-012345'
internet_gateway_id = 'igw-123456789'

ec2 = boto3.client('ec2')

ec2.create_route(DestinationCidrBlock='0.0.0.0/0', 
                GatewayId=internet_gateway_id, 
                RouteTableId=route_table_id)
