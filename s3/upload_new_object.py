import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket="zali-boto3-05012023", 
                Key="folder/foldera/folder1/test_text_string.txt", 
                Body="Hey this is a string", 
                ContentType="text/plain")