#!/bin/bash
# Det vore bra att skapa en kontroll om vpclisting.json finns. Ännu en sak som går att förbättra.
# CREATE TWO SEPERATE SUBNETS, one name finance and the other it. /19 Public Subnet, /20 Private Subnet.

# This will filter out and fetch the latest vpc id and store it to a variable.
VPCID= echo"$(jq  -r  '' vpclisting.json | grep \vpc-| sed /dl/d | sed s/'\s'//g | sed -e 's/\<VpcId\>//g'|tr -d '",:' | sed '$!d')"
#---------------------------------------------------------------------------------------------------------------------------
# Ip för första subnet
CIDR_BLOCK1= echo "10.0.0.1" # Bestämt värde, går att förbättra och göra det dynamiskt.
# Ip för sekundär subnet 
CIDR_BLOCK2= echo "10.0.127.1" #Bestämt värde, går att förbättra och göra det dynamiskt.
#---------------------------------------------------------------------------------------------------------------------------
AZ= echo "us-east-1a" # Om det inte funkar prova med något av följande(use1-az2, use1-az4, use1-az6)
REGION= echo "use.east-1" # Bestämt värde, går att förbättra och göra det dynamiskt.
#---------------------------------------------------------------------------------------------------------------------------
# Create first subnet

echo "$(aws ec2 create-subnet --vpc-id ${VPCID} --cidr-block ${CIDR_BLOCK1} --availability-zone ${AZ} --region ${REGION})"

# Create second subnet

echo "$(aws ec2 create-subnet --vpc-id ${VPCID} --cidr-block ${CIDR_BLOCK2} --availability-zone ${AZ} --region ${REGION})"

exit 
