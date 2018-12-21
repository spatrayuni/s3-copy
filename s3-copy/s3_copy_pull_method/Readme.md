
##Cross-Account Data Copy in S3 Using AWS Lambda
=================================================

Follow below steps to set up cross account access and deploy AWS Lambda function to enable cross account data copy from a S3 bucket in account A to another S3 bucket in account B.

Steps:
======


Set up IAM access and deploy Lambda functinons
------------------------------------------------

1. In destination AWS account, set up the IAM role and add trust relationship used to copy files from the source account and set up IAM policy and deploy Lambda function

    - Clone the repository.   
    - Set the source bucket name , destination bucket name, key, arn of destination account in the Lambda code s3_copy.py . Zip the code file and upload to the S3 bucket which will be used in Cloudformation to deploy Lambda function
    - Set the values S3 bucket, S3 key, arn of destination account in the Cloudformation template s3-copy.yaml 
    - Deploy the lambda function via Cloudformation using the below command,
        
        aws cloudformation create-stack --stack-name myteststack --template-body file://s3-copy.yaml --capabilities CAPABILITY_IAM
        
    - Deploy IAM role to use to copy file using the below command,
    
        aws cloudformation create-stack --stack-name myteststack --template-body file://IAM_Permissions.yaml --capabilities CAPABILITY_IAM    



2. In source AWS account, set up bucket policy to allow access to the IAM role used in the source destination.

    - Set the source bucket and destination account IAM role in in s3-bucket-policy.yaml
    - Deploy the IAM role using the below command,


         aws cloudformation create-stack --stack-name myteststack --template-body file://s3-bucket-policy.yaml --capabilities CAPABILITY_IAM




