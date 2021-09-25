#! /bin/bash
# I will comment out the sections that i have accoplished, it means that i have solved them in a seperate script. This file is just a general overview of the commands needed to accomplish the task.
# Getting AWS credentials from python script and inserting it to config file
#token = cat token.txt

#echo "token" | sudo tee ~/.aws/credentials
# This scrip is intented for setting up a cloud enviroment in AWS.
# Create .pem KEY, extra thing to solve: do i want one key for both or one each?

#echo aws ec2 create-key-pair --key-name <Key_Pair_Name> \ > --output text  > <Key_Pair_Name>.pem  
#echo chmod 400  <Key_Pair_name>.pem

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE VPC , Ideally, go for a /18 (16,382 IP adresses) or a /20 (4094 IP addresses) as your VPC network choice. 
#echo aws ec2 create-vpc --cidr-block <cidr_block> --region <region>
#echo aws ec2 describe-internet-gateways  
 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating An IGW
#echo aws ec2 create-internet-gateway


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Attaching An IGW to A VPC
#echo aws ec2 attach-internet-gateway --internet-gateway-id <IGWID> --vpc-id <VPCID> 


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#. Create Security Group   #for outbound rules e.g. : aws ec2 authorize-security-group-egress -group-id <securitygroupID> --protocol <protocol> --port <port> --cidr <cidr>

#.#. Get VPC ID
# echo aws ec2 describe-vpcs 

#.#. VPC
echo  aws ec2 create-security-group --group-name example --description "this is an example" --vpc-id <VPCID>

#.#. IT
echo  aws ec2 create-security-group --group-name example --description "this is an example" 
#.#. Add rules to IT - Security group
echo aws ec2 authorize-security-group-ingress --group name <SG_NAME> \ > --protocol <type> --port <number> --cidr 0.0.0.0/0

#.#.#. FINANCE
echo aws ec2 create-security-group --group-name example --description "this is an example"
#.#.#. Add rules to FINANCE - Security group
echo aws ec2 authorize-security-group-ingress --group name <SG_NAME> \ > --protocol <type> --port <number> --cidr 0.0.0.0/0

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE TWO SEPERATE SUBNETS, one name finance and the other it. /19 Public Subnet, /20 Private Subnet.

echo aws ec2 create-subnet --vpc-id <vpc_id> --cidr-block <cidr_block> --availability-zone <availability_zone> --region <region>

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE TWO EC2 instances, one in each subnet, specifies subnet and security group + key

echo aws ec2 run-instances --image-id <ID of the AMI> --count <number of instances> --instance type <type of the EC2 instance to be created --key-name = <Name of the existing key in the specified region> --security-group-ids = <ID of the existing security group in the specified region> --subnet-id <subnetid> --region <region>

echo aws ec2 run-instances --image-id <ID of the AMI> --count <number of instances> --instance type <type of the EC2 instance to be created --key-name = <Name of the existing key in the specified region> --security-group-ids = <ID of     the existing security group in the specified region> --subnet-id <subnetid> --region <region>



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE and ATTACH STORAGE
echo aws ec2 create-volume \ --size <size> --region <region> --availability-zone <region_abc> \ --volume-type gp2

echo aws ec2 attach-volume \ --volume-id <VolumeID> \ --instance-id <IID> \ /dev/sdg

#.#. echo unmount /dev/sdg
#.#.# echo aws ec2 detach-volume \ --volume-id <VolumeID>
#.#.#.#. echo aws ec2 delete-volume \ --volume-id <Volumeid>

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# CREATE ELLASTIC IP 

echo aws ec2 allocate-address --domain <domain> 

echo aws ec2 associate-address --network-interface-id <neid> --allocation-id <AID>


