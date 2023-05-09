import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for routeTable in response["RouteTables"]:
    print(routeTable["VpcId"])
    
for routeTable in response["RouteTables"]:
    print(routeTable["RouteTableId"])
    
for routeTable in response["RouteTables"]:
    for association in routeTable["Associations"]:
        if("SubnetId") in association:
            print(association["SubnetId"])
            
for routeTable in response["RouteTables"]:
    for association in routeTable["Associations"]:
        if("RouteTableAssociationId") in association:
            print(association["RouteTableAssociationId"])
        
for routeTable in response["RouteTables"]:
    for route in routeTable["Routes"]:
        print(route["DestinationCidrBlock"])
        
for routeTable in response["RouteTables"]:
    for route in routeTable["Routes"]:
        print(route["GatewayId"])