import boto3

ec2 = boto3.client('ec2')

ig = ec2.create_internet_gateway()

print(ig["InternetGateway"]["InternetGatewayId"])