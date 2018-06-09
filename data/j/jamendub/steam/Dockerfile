FROM debian:stretch-slim  
  
COPY sources.list /etc/apt/  
  
# install packages, add steam user and escalate  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y lib32gcc1 curl && \  
mkdir steam && cd steam && \  
curl -sqL
"https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar
-xvz  
  
WORKDIR steam  

