import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify instance ID and name for new AMI
instance_id = 'i-0123456789abcdef0'
ami_name = 'my-ami'

# Create AMI
response = ec2.create_image(InstanceId=instance_id, Name=ami_name)

# Print AMI ID
print(response['ImageId'])
