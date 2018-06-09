FROM ubuntu:14.04  
RUN apt-get update &&\  
apt-get install -y curl lib32gcc1 lib32stdc++6 && apt-get clean  
  
RUN mkdir -p /opt/steamcmd &&\  
cd /opt/steamcmd &&\  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz  
  
WORKDIR /opt/steamcmd  

