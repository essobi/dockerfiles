FROM ubuntu:14.04.2  
  
MAINTAINER minimum@cepave.com  
  
# Install Supervisor  
ONBUILD RUN \  
apt-get update && \  
apt-get install -y supervisor && \  
mkdir -p /var/log/supervisor && \  
apt-get clean && \  
rm -fR /tmp/*  

