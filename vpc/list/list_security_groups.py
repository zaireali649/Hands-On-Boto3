import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for securityGroup in response["SecurityGroups"]:
    print(securityGroup["GroupId"])
    
for securityGroup in response["SecurityGroups"]:
    print(securityGroup["VpcId"])
    
for securityGroup in response["SecurityGroups"]:
    print(securityGroup["GroupName"])
    
for securityGroup in response["SecurityGroups"]:
    print(securityGroup["Description"])
    
for securityGroup in response["SecurityGroups"]:
    for ipPermissions in securityGroup["IpPermissions"]:
        if "FromPort" in ipPermissions:
            print(ipPermissions["FromPort"])
        
for securityGroup in response["SecurityGroups"]:
    for ipPermissions in securityGroup["IpPermissions"]:
        print(ipPermissions["IpProtocol"])
        
for securityGroup in response["SecurityGroups"]:
    for ipPermissions in securityGroup["IpPermissions"]:
        if "ToPort" in ipPermissions:
            print(ipPermissions["ToPort"])
        
for securityGroup in response["SecurityGroups"]:
    for ipPermissions in securityGroup["IpPermissions"]:
        for ipRanges in ipPermissions["IpRanges"]:
            print(ipRanges["CidrIp"])
