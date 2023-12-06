#!/bin/bash

################
# Author: Pallavi

# Date: 06-12-2023

# Version V1

# This script is used to track the aws resources usage
################

# AWS S3
# AWS EC2
# AWS LAMBDA
# AWS IAM USERS

set -x

# List S3 buckets
aws s3 ls

#Get the list of all ec2 instances
aws ec2 describe-instances

#list lambda function
aws lambda list-functions

#list iam users
aws iam list-users
