import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify AMI ID to deregister
ami_id = 'ami-0123456789abcdef0'

# Deregister the AMI
response = ec2.deregister_image(ImageId=ami_id)

# Print response
print(response)
