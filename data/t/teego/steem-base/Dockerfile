# -*- coding: utf-8 -*-  
  
FROM debian:jessie  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "System updates" &&\  
( \  
apt-get update -q &&\  
apt-get upgrade -qy --no-install-recommends \  
) && \  
apt-get clean -qy  
  
RUN echo "Runtime requirements" &&\  
( \  
apt-get install -qy --no-install-recommends \  
coreutils \  
dnsutils \  
iputils-ping \  
ca-certificates \  
net-tools \  
iptables \  
figlet \  
wget \  
curl \  
bzip2 \  
unzip \  
zip \  
) && \  
apt-get clean -qy  
  
RUN figlet 'Ready!'  

