#!/bin/bash

##################
# Author : Pallavi

# Date : 02/12/23

# This script outputs the node health

# Version: v1
##################

set -x #debug mode
set -e #exits the script when there is an error
set -o pipefail #

df -h

free -g

nproc

