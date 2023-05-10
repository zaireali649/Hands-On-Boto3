import boto3

region_name = "us-east-1"

# Create EC2 client
ec2 = boto3.client('ec2', region_name=region_name)

# Retrieve list of AMIs
response = ec2.describe_images(Owners=['amazon'])

# Print list of AMIs
for image in response['Images']:
    print(image['ImageId'], image['Name'], image['CreationDate'])
