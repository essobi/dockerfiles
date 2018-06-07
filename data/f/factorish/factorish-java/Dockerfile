# Base Factorish Java Image  
#  
# Author: Paul Czarkowski  
# Date: 12/20/2014  
  
FROM java:7  
MAINTAINER Paul Czarkowski "paul@paulcz.net"  
# Base Deps  
RUN \  
apt-get update -yq && \  
apt-get install -yq \  
make \  
curl \  
ca-certificates \  
net-tools \  
sudo \  
wget \  
vim \  
strace \  
lsof \  
netcat \  
lsb-release \  
locales \  
socat \  
supervisor \  
runit \  
\--no-install-recommends && \  
locale-gen en_US.UTF-8  
# install etcdctl and confd  
RUN curl -sSL -o /usr/local/bin/etcdctl https://s3-us-
west-2.amazonaws.com/opdemand/etcdctl-v0.4.6 \  
&& curl -sSL -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-
amd64  
  
ADD my_init /usr/local/bin/my_init  
  
RUN \  
chmod +x /usr/local/bin/etcdctl \  
&& chmod +x /usr/local/bin/confd \  
&& chmod +x /usr/local/bin/my_init \  
&& mkdir /app  
  
WORKDIR /app  

