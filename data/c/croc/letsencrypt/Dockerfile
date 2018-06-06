FROM ubuntu:xenial  
  
RUN DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y
net-tools vim less curl letsencrypt  
  
VOLUME /etc/letsencrypt/  
  
COPY files/*.sh /opt/  
RUN chmod 755 /opt/*.sh  
  
ENTRYPOINT /bin/bash  

