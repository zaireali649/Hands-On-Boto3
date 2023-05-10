import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify security group name and description
sg_name = 'my-security-group'
sg_description = 'My security group'

# Create new security group
response = ec2.create_security_group(GroupName=sg_name, Description=sg_description)
sg_id = response['GroupId']

# Allow inbound traffic for SSH, HTTP, and HTTPS
ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        {'IpProtocol': 'tcp', 'FromPort': 443, 'ToPort': 443, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ]
)

# Print security group ID
print(f'Created security group {sg_id}')
