#!/bin/bash  
# Detta skript genererar en privat och en publik ssh nyckel

# Måste köras som root.
# Fråga efter input till key-namn
echo "what should your keyname be called?";

read 


echo "$(ssh-keygen -t rsa -C "${REPLY}" -f /home/xr/Dokument/permmissions/"${REPLY}")"

# Begränsa rättigheterna till den nya nyckeln.

echo "$(chmod 400 /home/xr/Dokument/permmissions/"${REPLY}")"

# detta kommando måste vara separat från root echo "$(aws ec2 import-key-pair --key-name "${REPLY}" --public-key-material fileb://~/Dokument/permmissions/"${REPLY}".pub)"

exit 
