import json
import boto3

def get_volume_id(volume_arn):
    arn_parts = volume_arn.split(':')
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    # Check if 'resources' is in the event
    if 'resources' not in event or not event['resources']:
        return {
            "statusCode": 400,
            "body": "Missing 'resources' in event"
        }
    
    volume_arn = event['resources'][0]
    volume_id = get_volume_id(volume_arn)
    
    ec2_client = boto3.client('ec2')

    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3'
    )
    
    return {
        "statusCode": 200,
        "body": f"Volume {volume_id} updated to gp3"
    }
