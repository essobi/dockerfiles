# Arch Linux container with gateone web ssh portal  
FROM greyltc/sshd-aur  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# install gateone  
ADD setup-gateone.sh /usr/sbin/setup-gateone  
RUN setup-gateone  
  
ADD run-gateone.sh /usr/bin/run-gateone  
  
CMD run-sshd; run-gateone; sleep infinity  

