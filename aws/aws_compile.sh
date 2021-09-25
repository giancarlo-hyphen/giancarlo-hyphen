#!/bin/bash

# * at the end of the comment means that the script is configured properly and can be called if all dependencies are met.

# / at the end of the comment means that the script needs to be tested.

# ? at the end of the comment means that the script is missing and needs to be created.

# What is the correct order for launching all scripts to avoid conflicts ?

# 1: Create VPC. ( call create_vpc.sh script) *


# 2: Create IGW and attach it to the VPC. ( call create_igw.sh) *



# 3: Create 2 subnets from the VPC. ( call create_vpc.sh) /


# 4: Generate  .pem keys. ( call pem_key_gen.sh) *


# 5: Import .pub keys to AWS ( call import_ssh_aws.ssh) *

# 5.1/2: Create AWS Elastic IP ?

# 6: Create EC2 Instances one for IT and one for finance and assignt it to corresponding subnet ?
# Create instance IT  ( Don't forget to assignt the elastic IP in this part) ?
 # Create instance Finance ?
 #6.a: Create security group for IT and assign rules ?
 #6.b: Create security group for Finance and assign rules ? 


# 7: Create security and assing rules for the security group ?

  #7.a: Finance  ( should not be available to access from the outside) ?

  #7.b: It ( should be available from the outside on port 80 and requires Elastic IP.) ?
  

# 8: Check and  Configure the routing tables for them to be correct. ?
