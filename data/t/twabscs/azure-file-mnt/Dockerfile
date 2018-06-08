FROM ubuntu:latest  
MAINTAINER Tom Armstrong  
  
RUN apt-get update && apt-get install -y \  
cifs-utils \  
curl \  
duplicity \  
git  
  
# troubleshooting tools  
RUN apt-get update && apt-get install -y \  
dnsutils \  
net-tools \  
iputils-ping \  
smbclient \  
tcpdump \  
telnet  
  
COPY ./azure-check.sh /  
  

