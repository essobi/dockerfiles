FROM ubuntu:latest  
  
  
RUN apt-get update  
  
RUN apt-get install -y \  
curl \  
net-tools \  
docker \  
build-essential \  
apt-utils \  
vim \  
mtr \  
traceroute \  
iputils-ping \  
awscli \  
groff \  
apache2-utils \  
netcat \  
wget \  
socat  
  
RUN cd /usr/bin && \  
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod a+x ./kubectl  
  
  

