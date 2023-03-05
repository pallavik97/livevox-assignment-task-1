import boto3
from datetime import datetime
import os
# AWS credentials and region
aws_access_key_id=os.environ['aws_access_key_id']
aws_secret_access_key=os.environ['aws_secret_access_key']

AWS_REGION = 'ap-south-1'

# Auto Scaling Group name
ASG_NAME = 'lv-test-cpu'

# Connect to AWS
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=AWS_REGION
)
asg_client = session.client('autoscaling')
ec2_client = session.client('ec2')

# Get Auto Scaling Group information
asg_response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[ASG_NAME])
asg = asg_response['AutoScalingGroups'][0]

# Get running instances information
instances = asg['Instances']
running_count = 0
for instance in instances:
    if instance['LifecycleState'] == 'InService':
        running_count += 1
        instance_id = instance['InstanceId']
        instance_response = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance_info = instance_response['Reservations'][0]['Instances'][0]
        print(f"Instance {instance_id} is running in {instance_info['Placement']['AvailabilityZone']} zone.")
        print(f"SecurityGroup: {instance_info['SecurityGroups'][0]['GroupId']}")
        print(f"ImageID: {instance_info['ImageId']}")
        print(f"VPCID: {instance_info['VpcId']}")
        launch_time = instance_info['LaunchTime']
        uptime = datetime.now(launch_time.tzinfo) - launch_time
        print(f"Uptime: {uptime}\n")

# Compare running count with desired capacity
desired_capacity = asg['DesiredCapacity']
if running_count == desired_capacity:
    print("Running count matches desired capacity.")
else:
    print("Running count does not match desired capacity.")

