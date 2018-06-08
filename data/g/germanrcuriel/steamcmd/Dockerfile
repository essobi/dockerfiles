FROM ubuntu:16.04  
MAINTAINER Germán Robledo <germix@germix.net>  
  
RUN apt-get update && \  
apt-get install -y curl lib32gcc1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /opt/steamcmd &&\  
cd /opt/steamcmd &&\  
curl -s https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
| tar -vxz  
  
ADD docker-entrypoint.sh /usr/local/bin  
  
ENTRYPOINT [ "docker-entrypoint.sh" ]  

