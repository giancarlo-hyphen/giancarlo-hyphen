#!/bin/bash

# Here you list your permissions

echo "$(ls -f /home/xr/Dokument/permmissions/*.pub)"

# Instruction printed
echo "Enter the  public key you are going to upload to aws"

# Read command use to stora character input in variabel 

read 

# Running the AWS command with variabel insertion


echo "$(aws ec2 import-key-pair --key-name "${REPLY}" --public-key-material fileb://~/Dokument/permmissions/"${REPLY}")"

exit 
