FROM khipu/base-ubuntu  
MAINTAINER developers@khipu.com  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install ntop -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 3000  
CMD /usr/sbin/ntop -L -u ntop -P /var/lib/ntop --access-log-
file=/var/log/ntop/access.log -i none -p /etc/ntop/protocol.list -O
/var/log/ntop  

