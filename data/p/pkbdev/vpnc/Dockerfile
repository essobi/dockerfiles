# For connecting to Cisco IPSec VPNs  
FROM ubuntu:14.04  
MAINTAINER mate@patientsknowbest.com  
  
RUN apt-get update  
RUN apt-get install -y vpnc openssh-client  
  
RUN apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD init.sh /  
  
CMD ["/init.sh"]  

