FROM khipu/base-ubuntu:latest  
MAINTAINER developers@khipu.com  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install curl s3cmd -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.6.3/confd-0.6.3-linux-
amd64 > /usr/local/bin/confd && \  
chmod +x /usr/local/bin/confd  

