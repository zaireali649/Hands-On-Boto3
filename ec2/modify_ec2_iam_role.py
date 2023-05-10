import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify instance ID and new IAM role
instance_id = 'i-0123456789abcdef0'
new_iam_role = 'my-new-iam-role'

# Modify instance attribute to update IAM role
response = ec2.modify_instance_attribute(
    InstanceId=instance_id,
    IamInstanceProfile={
        'Name': new_iam_role
    }
)

# Print response
print(response)
