import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_subnets()

for subnet in response["Subnets"]:
    print(subnet["CidrBlock"], subnet["SubnetId"], subnet["VpcId"])