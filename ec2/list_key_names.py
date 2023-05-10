import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Retrieve list of existing key pairs
response = ec2.describe_key_pairs()

# Print list of existing key pairs
for key_pair in response['KeyPairs']:
    print(key_pair['KeyName'], key_pair['KeyPairId'])
