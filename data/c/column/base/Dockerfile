FROM phusion/baseimage:0.9.21  
MAINTAINER Column Fang <column.fang@gmail.com>  
  
COPY files /  
  
RUN \  
# Remove ubuntu official source  
echo -n "" > /etc/apt/sources.list && \  
  
# Install tools  
apt-get update && \  
apt-get install -y git zip vim tree silversearcher-ag iproute2 iputils-ping &&
\  
  
# Config git  
git config --global user.name "Name" && \  
git config --global user.email "Email" && \  
  
# Cleanup  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  

