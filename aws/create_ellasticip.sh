#!/bin/bash

# CREATE ELLASTIC IP 
# Use the filter i created and catch "NetworkInterfaceID" e.g. "eni-b9a5ac93"


echo "$( aws ec2 allocate-address \ --domain vpc \ --network-border-group us-east-1| sudo tee allocationId.json)" # behöver jag lägga till något mer här ?


# Use the filter i created and catch "NetworkInterfaceID" e.g. "eni-b9a5ac93" is available from aws ec2 describe-instances output
NEID=

# Use the filter i created and catch " AllocationId" e.g. "eipalloc-02463d08ceEXAMPLE" is available from aws allocate adress output
AID= 

echo aws ec2 associate-address --network-interface-id <neid> --allocation-id <AID>

















exit 
