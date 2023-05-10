import boto3

route_table_id = "rtb-0022d08bba129c87b"
internet_gateway_id = "igw-0f91ffb69d289cc87"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)