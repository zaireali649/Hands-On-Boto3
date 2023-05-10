import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Specify AMI, instance type, key pair, IAM role, security group, and user data
ami_id = 'ami-0c55b159cbfafe1f0'
instance_type = 't2.micro'
key_name = 'my-key-pair'
security_group_ids = ['sg-0123456789abcdef0']
iam_role = 'my-iam-role'
user_data = 'echo "Hello World"'

# Launch new EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    IamInstanceProfile={
        'Name': iam_role
    },
    UserData=user_data
)

# Print instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f'Launched instance {instance_id}')
