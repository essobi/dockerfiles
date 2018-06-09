FROM ubuntu:15.04  
MAINTAINER cliffrowley@gmail.com  
  
RUN apt-get update && \  
apt-get install -q -y --no-install-recommends \  
ca-certificates \  
lib32gcc1 \  
net-tools \  
lib32stdc++6 \  
lib32z1 \  
lib32z1-dev \  
curl  
  
RUN mkdir -p /opt/steam/steamcmd && \  
curl -s https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
| tar -v -C /opt/steam/steamcmd -zx && \  
chown -R daemon:daemon /opt/steam  
  
WORKDIR /opt/steam/steamcmd  
USER daemon  
  
ADD install.sh /opt/steam/steamcmd/install.sh  

