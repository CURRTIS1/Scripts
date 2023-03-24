import boto3 

# Get a list of regions 
ec2_client = boto3.client('ec2') 
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']] 

# Check config recorder in each region 
for region_name in regions: 
    print(f"region_name : {region_name}") 
    config_client = boto3.client('config', region_name=region_name) 
    recorders = config_client.describe_configuration_recorders() 
    for configrecorder in recorders['ConfigurationRecorders']: 
        print(f"Config_recorder_name : {configrecorder['name']}") 
        print(f"Config_recorder_role_arn : {configrecorder['roleARN']}") 
        print(f"Config_recorder_global_resources : {configrecorder['recordingGroup']['includeGlobalResourceTypes']}") 
        print()