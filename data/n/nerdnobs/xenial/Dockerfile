FROM ubuntu:16.04  
MAINTAINER NerdNobs  
  
# set environment variables  
ARG DEBIAN_FRONTEND="noninteractive"  
ENV HOME="/data"  
ENV TERM="xterm"  
ENV NN_APP="xenial-base"  
COPY init /init  
# Set Up Environment  
RUN \  
# Service User  
useradd -u 5000 -U -d /data -s /bin/false bagman && \  
# Data Directory  
mkdir -p /data && \  
# Config Directory  
mkdir -p /data/config && \  
# Mounts Directory  
mkdir -p /data/mounts && \  
# Env Directory  
mkdir -p /data/env && \  
# Service Directory  
mkdir -p /etc/service && \  
# Update Image  
apt-get update && \  
apt-get upgrade -y && \  
# Install Standard Packages  
apt-get install -y apt-utils runit curl wget python2.7 && \  
# Symlink Python  
ln -s /usr/bin/python2.7 /usr/bin/python && \  
chmod +x /init && \  
# Cleanup  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
  
# Clean Up .keep files  
RUN find / -name .keep -exec rm -rf {} \;  
  
ENTRYPOINT ["/init"]

