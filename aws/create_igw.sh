#!/bin/bash

# Creating IGW
echo "$(aws ec2 create-internet-gateway )"

echo "$(aws ec2 describe-internet-gateways | sudo tee igwlisting.json )"

# Om du behöver plocka upp ett visst IGW-nummer i listan. Ändra då 1p till 2p t.ex. 
# IGWID= echo "$(jq  -r  '' igwlisting.json | grep \igw-| sed /dl/d | sed s/'\s'//g | sed -e 's/\<InternetGatewayId\>//g'|tr -d '",:' | sed -n 1p)"

# Filtrerar variabeln till den senast skapade IGW:n
IGWID= echo "$(jq  -r  '' igwlisting.json | grep \igw-| sed /dl/d | sed s/'\s'//g | sed -e 's/\<InternetGatewayId\>//g'|tr -d '",:' | sed '$!d')"

# Filtrerar varibeln till den senast skapade VPC:n
VPCID= echo "$(jq  -r  '' vpclisting.json | grep \vpc-| sed /dl/d | sed s/'\s'//g | sed -e 's/\<VpcId\>//g'|tr -d '",:' | sed '$!d')"


# Attaching the IGW to VPC

echo "$(aws ec2 attach-internet-gateway --internet-gateway-id ${IGWID} --vpc-id ${VPCID})"



exit 
