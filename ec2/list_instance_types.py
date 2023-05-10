import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Retrieve list of available instance types
response = ec2.describe_instance_types()

# Print list of available instance types
for instance_type in response['InstanceTypes']:
    print(instance_type['InstanceType'])
