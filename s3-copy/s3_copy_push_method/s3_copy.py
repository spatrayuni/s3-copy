import json
import boto3

#Set source and destination bucket names and key 
source = "source-bucket-name"
destination ="destination-bucket-name"
key = "key/pattern of file to copy from souce to destination"

def handler(event, context):
    
   #assume role of destination account to copy files, 
   #this way the owner of the file will be destination role    
   sts_client = boto3.client('sts')
   assumedRoleObject = sts_client.assume_role(
   RoleArn="arn of role used to copy files in destination account",
   RoleSessionName="AssumeRoleSession1")
   credentials = assumedRoleObject['Credentials']
   print(credentials)
   
   #instantiate S3 using the destination accont role
   s3 = boto3.client(
       's3',
        aws_access_key_id = credentials['AccessKeyId'],
        aws_secret_access_key = credentials['SecretAccessKey'],
        aws_session_token = credentials['SessionToken'],

     )
   copy_data = {
    'Bucket': source,
    'Key': key}
   s3.copy_object(Bucket=destination, Key=key, CopySource=copy_data)
 
    