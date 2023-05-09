import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_vpcs()

vpcs = response["Vpcs"]

for vpc in vpcs:
    print(vpc['VpcId'])
    
for vpc in vpcs:
    print(vpc['CidrBlock'])
    
for vpc in vpcs:
    print(vpc['IsDefault'])

for vpc in vpcs:
    if "Tags" in vpc:
        for tag in vpc['Tags']:
            if tag['Key'] == 'Name':
                vpc_name = tag['Value']

filters = [{'Name':'isDefault', 'Values':['true']}]
response = ec2.describe_vpcs(Filters=filters)

for vpc in response["Vpcs"]:
    print(vpc['IsDefault'])