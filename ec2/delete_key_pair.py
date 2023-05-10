import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify key pair name to delete
key_name = 'my-key-pair'

# Delete the key pair
response = ec2.delete_key_pair(KeyName=key_name)

# Print response
print(response)
