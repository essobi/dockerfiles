FROM tcf909/ubuntu-slim  
MAINTAINER T.C. Ferguson <tcf909@gmail.com>  
  
#OPENVPN  
RUN \  
apt-get update && \  
apt-get install iptables iproute2 && \  
#CLEANUP  
apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY start /  
  
CMD ["/start"]  

