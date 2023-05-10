import boto3

route_table_id = "rtb-0022d08bba129c87b"

ec2 = boto3.client('ec2')

ec2.delete_route_table(
    RouteTableId=route_table_id,
)