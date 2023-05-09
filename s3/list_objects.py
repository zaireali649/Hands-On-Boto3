import boto3

def filter_objects_extension(client, bucket, extension):
    keys = []
    response = client.list_objects_v2(Bucket=bucket)
    for content in response["Contents"]:
        if(extension in content["Key"][-(len(extension)):]):
            keys.append(content["Key"])
            
    return keys
    
def list_object_keys(client, bucket, prefix=""):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response["Contents"]:
        keys.append(content["Key"])
            
    return keys


if __name__ == '__main__':
    s3 = boto3.client('s3')
    
    response = list_object_keys(s3, "zali-boto3-05012023", "folder/")
    print(response)
    
    
    response = filter_objects_extension(s3, "zali-boto3-05012023", "/")
    print(response)
