import boto3

route_table_id = 'rtb-0022d08bba129c87b'
subnet_id = 'subnet-0bd7e74203e0f1a09'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])