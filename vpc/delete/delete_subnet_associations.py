import boto3

associationId = "rtbassoc-01234"

# Create EC2 client
ec2 = boto3.client('ec2')

ec2.disassociate_route_table(AssociationId=associationId)