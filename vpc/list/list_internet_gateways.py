import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_internet_gateways()

for internetGateway in response["InternetGateways"]:
    print(internetGateway["InternetGatewayId"])
    
for internetGateway in response["InternetGateways"]:
    for attachment in internetGateway["Attachments"]:
        print(attachment["State"])
        
for internetGateway in response["InternetGateways"]:
    for attachment in internetGateway["Attachments"]:
        print(attachment["VpcId"])