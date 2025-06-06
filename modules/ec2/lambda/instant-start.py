import boto3
import os

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = os.environ['INSTANCE_ID']
    
    response = ec2.start_instances(
        InstanceIds=[instance_id]
    )
    
    return {
        'statusCode': 200,
        'body': f'Successfully started instance {instance_id}'
    }
