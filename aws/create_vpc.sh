#!/bin/bash
#This script is intented to create a VPC in AWZ.

#Region variable, can be improved by setting the user as a variable so it can easily be deployed on different computers.
region="$(cd /home/xr/.aws; cat config | grep -o -P -m 1 -h -r  'us-.{0,7}' | grep us-| head -1)";

echo " CREATE VPC , Ideally, go for a /18 (16,382 IP adresses) or a /20 (4094 IP addresses) as your VPC network choice. class a: 10.0.0.1/18 , class b: 172.16.0.1/20  class c:192.168.0.1/24 " 


read 


echo "$(aws ec2 create-vpc --cidr-block "${REPLY}" --region "${region}")"

echo "$(aws ec2 describe-internet-gateways | sudo tee vpclisting.json)"

exit 
